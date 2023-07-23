from .model import QuoteModel
from typing import List
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Abstract class for Ingestor classes."""

    extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Check if file can be ingested."""
        ext = path.split('.')[-1]
        return ext in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from different types of files."""
        pass
