import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    """Configuration class for the data retrieval service from environment variables"""
    # Path
    local_folder_path: str

    # Kafka
    kafka_bootstrap_servers: str
    kafka_topic_name: str

    @classmethod
    def from_env(cls) -> "Config":
        """Create a Config object from environment variables"""
        load_dotenv()

        local_folder_path = os.getenv("LOCAL_FOLDER_PATH")

        kafka_bootstrap_servers = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
        kafka_topic_name = os.getenv("KAFKA_TOPIC_NAME", "files_details")

        return cls(
            local_folder_path=local_folder_path,
            kafka_bootstrap_servers=kafka_bootstrap_servers,
            kafka_topic_name=kafka_topic_name
        )