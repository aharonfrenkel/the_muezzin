from elasticsearch import Elasticsearch


class ElasticsearchService:
    def __init__(self, connection_string: str):
        """Initializes the Elasticsearch client"""
        self._client = Elasticsearch(connection_string)

    # CRUD operations
    def update_document_by_id(self, index_name: str, doc_id: str, data: dict, **kwargs) -> bool:
        """
        Updates a document in the index by id

        Args:
             index_name: Name of the index to update
             doc_id: The id of the document
             data: Fields data to update
             kwargs: Additional keyword arguments

        Returns:
            True if the document was updated, False otherwise
        """
        try:
            response = self._client.update(index=index_name, id=doc_id, doc=data, **kwargs)
            return response.get('result') == 'updated'
        except Exception:
            return False