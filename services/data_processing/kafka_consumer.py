import json
from typing import Any

from kafka import KafkaConsumer


class KafkaConsumerService:
    def __init__(self, bootstrap_servers: str, group_id: str = None):
        """Initialize the Kafka consumer client"""
        self._consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            key_deserializer=lambda k: json.loads(k.decode("utf-8")) if k is not None else None,
            auto_offset_reset='earliest',
            enable_auto_commit=True
        )

    def subscribe(self, *topics: str) -> None:
        """
        Subscribe to one or more topics

        Args:
            *topics: One or more topics to subscribe to
        """
        self._consumer.subscribe(topics)

    def poll_events(self, timeout_ms: int = 1000) -> list[dict[str, Any]]:
        """
        Poll for events from subscribed topics

        Args:
            timeout_ms: Maximum time to wait for events

        Returns:
            List of event dictionaries
        """
        events = []

        message_batch = self._consumer.poll(timeout_ms)

        for _, records in message_batch.items():
            for record in records:
                events.append(record.value)

        return events


    def close(self) -> None:
        self._consumer.close()