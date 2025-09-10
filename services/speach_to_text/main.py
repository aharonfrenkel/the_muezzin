from mongodb_service import MongoDBService
from elasticsearch_service import ElasticsearchService
from audio_transcriber import AudioTranscriber
from config import Config


def main() -> None:
    config = Config.from_env()

    mongodb_service = MongoDBService(config.mongodb_uri, config.mongodb_database_name)
    files_cursor = mongodb_service.get_files()

    elasticsearch_service = ElasticsearchService(config.elasticsearch_uri)
    elasticsearch_index_name = config.elasticsearch_index_name

    audio_transcriber = AudioTranscriber()

    for file in files_cursor:
        file_id = file._id
        file_content = file.read()

        audio_text = audio_transcriber.transcribe(file_content)

        elasticsearch_service.update_document_by_id(
            index_name=elasticsearch_index_name,
            doc_id=file_id,
            data={"audio_text": audio_text}
        )

if __name__ == "__main__":
    main()