from Exceptions import InvalidFileFormatException
from typing import List
from .model import QuoteModel
from .IngestorInterface import IngestorInterface
import docx


class DocxIngestor(IngestorInterface):
    """Class to represent docx ingestor."""

    extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from docx file."""
        if not cls.can_ingest(path):
            raise InvalidFileFormatException("Invalid file format")

        quotes = []
        doc = docx.Document(path)
        lines = [para.text for para in doc.paragraphs]

        quotes = cls.parse_lines(lines)

        return quotes

    @classmethod
    def parse_lines(cls, lines: List[str]) -> List[QuoteModel]:
        """Parse quotes from list of lines."""
        quotes = []
        for line in lines:
            if " - " in line:
                quote = QuoteModel(*line.strip().split(" - "))
                quotes.append(quote)
        return quotes
