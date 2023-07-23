from Exceptions import InvalidFileFormatException
from typing import List
from .model import QuoteModel
from .IngestorInterface import IngestorInterface
import subprocess
import tempfile
import os


class PDFIngestor(IngestorInterface):
    """Class to represent pdf ingestor."""

    extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from pdf file."""
        if not cls.can_ingest(path):
            raise InvalidFileFormatException("Invalid file format")

        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
            subprocess.call(['pdftotext', '-layout', path, tmp.name])
            tmp.seek(0)
            lines = tmp.readlines()

        quotes = cls.parse_lines(lines)
        os.remove(tmp.name)

        return quotes

    @classmethod
    def parse_lines(cls, lines: List[str]) -> List[QuoteModel]:
        """Parse quotes from list of lines."""
        quotes = []
        for line in lines:
            line = line.strip('\n\r').strip()
            if len(line) > 0 and " - " in line:
                quote = QuoteModel(*line.strip().split(" - "))
                quotes.append(quote)
        return quotes
