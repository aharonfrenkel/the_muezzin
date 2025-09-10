import os
from dataclasses import dataclass

from dotenv import load_dotenv

@dataclass
class Config:
    """Configuration class for the data investigator service from environment variables"""
    # Elasticsearch
    elasticsearch_uri: str
    elasticsearch_index_name: str

    # Hostile words
    hostile_words: str
    extremely_hostile_words: str

    @classmethod
    def from_env(cls) -> "Config":
        """Create a Config object from environment variables"""
        load_dotenv()

        elasticsearch_uri = os.getenv("ELASTICSEARCH_URI", "http://localhost:9200")
        elasticsearch_index_name = os.getenv("ELASTICSEARCH_INDEX_NAME", "files_metadata")

        hostile_words = os.getenv("HOSTILE_WORDS", "")
        extremely_hostile_words = os.getenv("EXTREMELY_HOSTILE_WORDS", "")

        return cls(
            elasticsearch_uri=elasticsearch_uri,
            elasticsearch_index_name=elasticsearch_index_name,

            hostile_words=hostile_words,
            extremely_hostile_words=extremely_hostile_words
        )