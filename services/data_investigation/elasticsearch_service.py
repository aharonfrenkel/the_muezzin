from typing import Any

from elasticsearch import Elasticsearch


class ElasticsearchService:
    def __init__(self, connection_string: str):
        """Initializes the Elasticsearch client"""
        self._client = Elasticsearch(connection_string)

    # CRUD operations
    def search(
            self,
            index_name: str,
            query_body: dict,
            source: list[str] = None,
            **kwargs
    ) -> dict[str, Any]:
        """
        Searches for documents in the index

        Args:
             index_name: name of the index
             query_body: query body
             source: list of fields to return
             kwargs: additional keyword arguments

        Returns:
            search result as a dictionary
        """
        try:
            response = self._client.search(
                index=index_name,
                query=query_body,
                source=source,
                **kwargs
            )
            return response
        except Exception:
            return False

    def update_document_by_id(self, index_name: str, doc_id: str, data: dict, **kwargs) -> bool:
        """
        Args:
             index_name: name of the index
             doc_id
             data
             kwargs: additional keyword arguments

        Returns:
            True if the document was updated, False otherwise
        """
        try:
            response = self._client.update(index=index_name, id=doc_id, doc=data, **kwargs)
            return response.get('result') == 'updated'
        except Exception:
            return False

    @classmethod
    def build_base_bool_query(cls, min_should_match: int = 1):
        base_bool_query = {
            "bool": {
                "should": [],
                "must": [],
                "filter": [],
                "must_not": [],
                "minimum_should_match": min_should_match
            }
        }
        return base_bool_query

    @classmethod
    def build_match_query_clauses(
            cls,
            expressions: list[str],
            filed_name: str,
            constant_score: bool = False,
            boost: float = 1.0
    ):
        query = []

        for expression in expressions:
            if ' ' in expression:
                filter_query = {
                    "match_phrase": {
                        filed_name: expression
                    }
                }
            else:
                filter_query = {
                    "match": {
                        filed_name: expression
                    }
                }
            if not constant_score:
                query.append(filter_query)
            else:
                constant_score_query = {
                    "constant_score": {
                        "filter": filter_query,
                        "boost": boost
                    }
                }
                query.append(constant_score_query)
        return query