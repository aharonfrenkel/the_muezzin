from pathlib import Path
from typing import Any


class FileRetrieval:
    def __init__(self, file_path: str):
        """Initialize the FileRetrieval object"""
        self._file_path = self._validate_file_path(file_path)

    def get_file_path(self) -> str:
        """Get the file path as a string"""
        return str(self._file_path)

    def get_file_metadata(self) -> dict[str, Any]:
        """Get the file metadata as a dictionary"""
        file_metadata = self._file_path.stat()

        result = {
            "file_name": self._file_path.name,
            "file_size": file_metadata.st_size,
            "file_creation_timestamp": file_metadata.st_ctime_ns
        }

        return result

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

git_commit = """
add file retrieval class

- add FileRetrieval class
- add get_file_path method
- add get_file_metadata method
"""