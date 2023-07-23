from Exceptions import InvalidFileFormatException
from typing import List
from .model import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """Class to represent text ingestor."""

    extensions = ['txt']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Parse quotes from txt file."""
        if not cls.can_ingest(path):
            raise InvalidFileFormatException("Invalid file format")

        with open(path, "r") as f:
            lines = f.readlines()

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
