from typing import Any

from file_retrieval import FileRetrieval


class DataProcessor:
    def __init__(self, file_retrieval: FileRetrieval):
        """Initialize the FileProcessor object"""
        self._file_retrieval = file_retrieval

    def get_file_data_json(self) -> dict[str, Any]:
        """Get the file data as a JSON object"""
        file_path = self._file_retrieval.get_file_path()
        file_metadata = self._file_retrieval.get_file_metadata()

        return {
            "file_path": file_path,
            "file_metadata": file_metadata
        }