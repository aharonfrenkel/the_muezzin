import uuid
from typing import Any


class DataProcessor:
    def __init__(self, record_value: dict[str, Any]):
        self._record_value = record_value

    def generate_unique_id(self, field: str = "file_path") -> str:
        """
        Generate unique ID based on a field in the record (default is file_path)

        Args:
            field: The field to use for generating the unique ID

        Returns:
            A unique ID based on the field value
        """
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, self._record_value.get(field)))

    def extract_file_content(self) -> bytes:
        """Extract the file content from the file path in the record"""
        return open(self._record_value.get("file_path"), "rb").read()