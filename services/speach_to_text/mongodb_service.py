from gridfs import GridFS, GridOutCursor
from pymongo import MongoClient


class MongoDBService:
    def __init__(self, connection_string: str, db_name: str):
        """Initializes the MongoDB client"""
        self._client = MongoClient(connection_string)
        self._db = self._client[db_name]
        self._fs = GridFS(self._db)

    # CRUD operations
    def get_files(self) -> GridOutCursor:
        """Get GridOutCursor object for iterate over the files"""
        return self._fs.find()