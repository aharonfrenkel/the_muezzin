import json
from typing import Any

from kafka import KafkaProducer


class KafkaProducerService:
    def __init__(self, bootstrap_servers: str):
        """Initialize the Kafka producer client"""
        self._producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=str).encode("utf-8"),
            key_serializer=lambda k: json.dumps(k, default=str).encode("utf-8") if k is not None else None
        )

    def send(self, topic: str, value: Any) -> None:
        """
        Send an event to a Kafka topic

        Args:
            topic: The name of the topic to send the evnet to
            value: The value of the event
        """
        self._producer.send(topic, value)

    def _flush(self) -> None:
        self._producer.flush()

    def close(self) -> None:
        self._flush()
        self._producer.close()