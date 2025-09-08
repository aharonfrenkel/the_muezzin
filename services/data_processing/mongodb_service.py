from typing import Optional

from gridfs import GridFS
from pymongo import MongoClient


class MongoDBService:
    def __init__(self, connection_string: str, db_name: str):
        """Initializes the MongoDB client"""
        self._client = MongoClient(connection_string)
        self._db = self._client[db_name]
        self._fs = GridFS(self._db)

    # CRUD operations
    def insert_file(
            self,
            file_content: bytes,
            _id: Optional[str] = None,
            **kwargs
    ) -> bool:
        """
        Insert a file into the GridFS bucket

        Args:
            file_content: File content to insert
            _id: A unique id for the file
            kwargs: Additional keyword arguments

        Returns:
            True if the file was inserted, False otherwise
        """
        try:
            if _id:
                self._fs.put(file_content, _id=_id, **kwargs)
            else:
                self._fs.put(file_content, **kwargs)
            return True
        except Exception:
            return False