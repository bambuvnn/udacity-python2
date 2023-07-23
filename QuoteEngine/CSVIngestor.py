from Exceptions import InvalidFileFormatException
from typing import List
from .model import QuoteModel
from .IngestorInterface import IngestorInterface
import pandas


class CSVIngestor(IngestorInterface):
    """Class to represent csv ingestor."""

    required_columns = ['body', 'author']
    extensions = ['csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if csv file can be ingested."""
        if not super().can_ingest(path):
            return False

        try:
            df = pandas.read_csv(path, header=0)
            cls.validate_columns(df.columns)
            return True
        except InvalidFileFormatException:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse quotes from csv file."""
        df = pandas.read_csv(path, header=0)
        quotes = [QuoteModel(row['body'], row['author'])
                  for _, row in df.iterrows()]

        return quotes

    @classmethod
    def validate_columns(cls, columns: List[str]):
        """Validate required columns exist in csv."""
        for col in cls.required_columns:
            if col not in columns:
                raise Exception(f"Missing required column: {col}")
