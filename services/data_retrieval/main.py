import os

from file_details_processor import FileDetailsProcessor
from file_details_retrieval import FileDetailsRetrieval
from kafka_producer import KafkaProducerService
from services.data_retrieval.config import Config


def main() -> None:
    config = Config.from_env()

    kafka_producer = KafkaProducerService(config.kafka_bootstrap_servers)

    for file in os.listdir(config.local_folder_path):
        file_path = os.path.join(config.local_folder_path, file)
        file_details = FileDetailsRetrieval(file_path)
        data_processor = FileDetailsProcessor(file_details)
        kafka_producer.send(
            topic=config.kafka_topic_name,
            value=data_processor.get_file_details()
        )

    kafka_producer.close()

if __name__ == "__main__":
    main()