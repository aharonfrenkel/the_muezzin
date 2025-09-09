import os
from typing import Callable, Any

from dotenv import load_dotenv

from logger import Logger


load_dotenv()


logger = Logger.get_logger(
    name=os.getenv("LOGGER_NAME"),
    es_host=os.getenv("ELASTICSEARCH_URI"),
    index=os.getenv("ELASTICSEARCH_INDEX_NAME")
)


def log(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        func_name = func.__name__
        try:
            result = func(*args, *kwargs)
            logger.info(f"{func_name} with args: {args} and kwargs: {kwargs} finished successfully")
            return result
        except Exception as e:
            logger.error(f"{func_name}: with args: {args} and kwargs: {kwargs} failed with error: {e}")
    return wrapper