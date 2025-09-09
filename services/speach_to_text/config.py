import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration class for the speach-to-text service from environment variables"""
    # MongoDB
    mongodb_uri: str
    mongodb_database_name: str

    # Elasticsearch
    elasticsearch_uri: str
    elasticsearch_index_name: str

    @classmethod
    def from_env(cls) -> "Config":
        """Create a Config object from environment variables"""
        load_dotenv()

        mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
        mongodb_database_name = os.getenv("MONGODB_DATABASE_NAME", "files_data")

        elasticsearch_uri = os.getenv("ELASTICSEARCH_URI", "http://localhost:9200")
        elasticsearch_index_name = os.getenv("ELASTICSEARCH_INDEX_NAME", "files_metadata")

        return cls(
            mongodb_uri=mongodb_uri,
            mongodb_database_name=mongodb_database_name,

            elasticsearch_uri = elasticsearch_uri,
            elasticsearch_index_name = elasticsearch_index_name
        )