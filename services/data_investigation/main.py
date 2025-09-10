from config import Config
from decode import decode_base64
from elasticsearch_service import ElasticsearchService
from text_investigation import TextInvestigator


def main() -> None:
    config = Config.from_env()

    elasticsearch_service = ElasticsearchService(config.elasticsearch_uri)

    hostile_words = decode_base64(config.hostile_words).split(",")
    extremely_hostile_words = decode_base64(config.extremely_hostile_words).split(",")

    text_investigator = TextInvestigator(elasticsearch_service, hostile_words, extremely_hostile_words)
    text_investigator.calculate_percent_danger(config.elasticsearch_index_name, "audio_text")


if __name__ == '__main__':
    main()