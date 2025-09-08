from os import stat_result
from pathlib import Path
from typing import Any

from file_details_retrieval import FileDetailsRetrieval


class FileDetailsProcessor:
    def __init__(self, file_details: FileDetailsRetrieval):
        """Initialize the FileProcessor object"""
        self._file_details = file_details

    def get_file_details(self) -> dict[str, Any]:
        """Get the file details as a JSON object"""
        file_path: str = str(self._file_details.path)
        file_metadata: dict[str, Any] = self._process_file_metadata_to_json()

        result = {
            "file_path": file_path,
            "file_metadata": file_metadata
        }

        return result

    def _process_file_metadata_to_json(self) -> dict[str, Any]:
        """Process the file metadata to JSON object"""
        file_path: Path = self._file_details.path
        file_metadata: stat_result = self._file_details.metadata

        result = {
            "file_name": file_path.name,
            "file_size": file_metadata.st_size,
            "file_creation_timestamp": file_metadata.st_ctime_ns
        }

        return result