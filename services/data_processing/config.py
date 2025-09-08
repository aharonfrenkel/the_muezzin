import os
from dataclasses import dataclass

from dotenv import load_dotenv

@dataclass
class Config:
    """Configuration class for the data processing service from environment variables"""
    # Kafka
    kafka_bootstrap_servers: str
    kafka_topic_name: str

    # Elasticsearch
    elasticsearch_uri: str
    elasticsearch_index_name: str

    # MongoDB
    mongodb_uri: str
    mongodb_database_name: str

    @classmethod
    def from_env(cls) -> "Config":
        """Create a Config object from environment variables"""
        load_dotenv()

        kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        kafka_topic_name = os.getenv("KAFKA_TOPIC_NAME", "files_details")

        elasticsearch_uri = os.getenv("ELASTICSEARCH_URI", "http://localhost:9200")
        elasticsearch_index_name = os.getenv("ELASTICSEARCH_INDEX_NAME", "files_metadata")

        mongodb_uri = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
        mongodb_database_name = os.getenv("MONGODB_DATABASE_NAME", "files_data")

        return cls(
            kafka_bootstrap_servers=kafka_bootstrap_servers,
            kafka_topic_name=kafka_topic_name,

            elasticsearch_uri=elasticsearch_uri,
            elasticsearch_index_name=elasticsearch_index_name,

            mongodb_uri=mongodb_uri,
            mongodb_database_name=mongodb_database_name
        )