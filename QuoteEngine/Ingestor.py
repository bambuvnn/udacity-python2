"""Module that Encapsulate moduels for ingest differnt types of files."""
from .model import QuoteModel
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .IngestorInterface import IngestorInterface
from typing import List


class Ingestor(IngestorInterface):
    """Class to represent Ingestor."""

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from different types of files."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

    @classmethod
    def parse_files(cls, files: List[str]) -> List[QuoteModel]:
        quotes = []
        for file in files:
            for ingestor in cls.ingestors:
                if ingestor.can_ingest(file):
                    quotes.extend(ingestor.parse(file))
        return quotes
