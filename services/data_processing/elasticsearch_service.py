from typing import Any, Optional

from elasticsearch import Elasticsearch


class ElasticsearchService:
    def __init__(self, connection_string: str):
        """Initializes the Elasticsearch client"""
        self._client = Elasticsearch(connection_string)

    # Indices management
    def create_index(self, index_name: str, mapping: Optional[dict[str, Any]] = None, **kwargs) -> bool:
        """
        Creates an index if it doesn't exist

        Args:
            index_name: Name of the index to create
            mapping: Mapping of the index fields
            kwargs: Additional keyword arguments

        Returns:
            True if the index was created, False otherwise
        """
        try:
            self._client.indices.create(index=index_name, mappings=mapping, **kwargs)
            return True
        except Exception as e:
            print(e)
            return False

    # CRUD operations
    def insert_document(self, index_name: str, doc: dict[str, Any], _id: str, **kwargs) -> bool:
        """
        Insert a document into the index

        Args:
            index_name: Name of the index
            doc: Document to insert
            _id: A unique id for a document
            kwargs: Additional keyword arguments

        Returns:
            True if the document was inserted, False otherwise
        """
        try:
            self._client.index(index=index_name, body=doc, id=_id, **kwargs)
            return True
        except Exception:
            return False