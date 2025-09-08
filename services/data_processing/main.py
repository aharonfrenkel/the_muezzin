from kafka_consumer import KafkaConsumerService
from elasticsearch_service import ElasticsearchService
from mongodb_service import MongoDBService
from data_processor import DataProcessor
from config import Config


def main() -> None:
    config = Config.from_env()

    kafka_consumer_service = KafkaConsumerService(config.kafka_bootstrap_servers)
    kafka_consumer_service.subscribe(config.kafka_topic_name)
    events = kafka_consumer_service.poll_events()
    kafka_consumer_service.close()

    elasticsearch_service = ElasticsearchService(config.elasticsearch_uri)
    elasticsearch_service.create_index(config.elasticsearch_index_name)

    mongodb_service = MongoDBService(config.mongodb_uri, config.mongodb_database_name)

    for event in events:
        data_processor = DataProcessor(event)
        unique_id = data_processor.generate_unique_id()
        file_content = data_processor.extract_file_content()

        elasticsearch_service.insert_document(
            index_name=config.elasticsearch_index_name,
            doc=event.get("file_metadata"),
            _id=unique_id
        )
        mongodb_service.insert_file(
            file_content=file_content,
            _id=unique_id
        )

if __name__ == "__main__":
    main()