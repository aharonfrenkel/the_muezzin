from typing import Any

from elasticsearch_service import ElasticsearchService


class TextInvestigator:
    def __init__(
            self,
            elasticsearch_service: ElasticsearchService,
            hostile_words: list[str] = None,
            extremely_hostile_words: list[str] = None
    ):
        self._elasticsearch_service = elasticsearch_service
        self.hostile_words = hostile_words
        self.extremely_hostile_words = extremely_hostile_words

    def get_negative_podcasts(self, index_name: str, field_name: str) -> dict[str, Any]:
        query = ElasticsearchService.build_base_bool_query()

        query["bool"]["should"].extend(
            ElasticsearchService.build_match_query_clauses(
                self.hostile_words, field_name, constant_score=True
            )
        )
        query["bool"]["should"].extend(
            ElasticsearchService.build_match_query_clauses(
                self.extremely_hostile_words, field_name, constant_score=True, boost=2.0
            )
        )

        return self._elasticsearch_service.search(index_name=index_name, query_body=query, source=[field_name])

    def calculate_percent_danger(self, index_name: str, field_name: str) -> None:
        negative_podcasts = self.get_negative_podcasts(index_name, field_name)
        max_score = negative_podcasts['hits']['max_score']

        for podcast in negative_podcasts['hits']['hits']:
            podcast_id = podcast['_id']
            podcast_score = podcast['_score']
            podcast_percent_danger = podcast_score / max_score * 100
            self._elasticsearch_service.update_document_by_id(
                index_name=index_name,
                doc_id=podcast_id,
                data={
                    "bds_percent": podcast_percent_danger
                }
            )