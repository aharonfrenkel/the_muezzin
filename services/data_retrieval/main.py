import os

from dotenv import load_dotenv

from data_processor import DataProcessor
from file_retrieval import FileRetrieval
from kafka_producer import KafkaProducerService


load_dotenv()


FOLDER_PATH = os.getenv("FOLDER_PATH", r"C:\Users\User\Desktop\podcasts")
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "file_metadata")


def main() -> None:
    kafka_producer = KafkaProducerService(BOOTSTRAP_SERVERS)

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)
        file_retrieval = FileRetrieval(file_path)
        data_processor = DataProcessor(file_retrieval)
        kafka_producer.send(
            topic=KAFKA_TOPIC,
            value=data_processor.get_file_data_json()
        )
    kafka_producer.close()

if __name__ == "__main__":
    main()