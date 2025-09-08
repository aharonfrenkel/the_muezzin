from pathlib import Path
from typing import Any


class FileDetailsRetrieval:
    def __init__(self, file_path: str):
        """Initialize the FileRetrieval object"""
        self._file_path = self._validate_file_path(file_path)
        self._file_metadata = self._file_path.stat()

    @property
    def path(self) -> str:
        """Get the file path as a string"""
        return self._file_path

    @property
    def metadata(self) -> dict[str, Any]:
        """Get the file metadata as a dictionary"""
        return self._file_metadata

    @staticmethod
    def _validate_file_path(file_path) -> Path:
        """
        Validate that the file path exists and is a file

        Args:
            file_path: path to the file

        Returns:
            Path object
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError("File does not exist")
        if not path.is_file():
            raise ValueError("Path is not a file")

        return path