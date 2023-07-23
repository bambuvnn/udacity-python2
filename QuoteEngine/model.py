class QuoteModel:
    """Class to represent quote model."""

    def __init__(self, body, author):
        """Quote model constructor."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return string representation of QuoteModel."""
        return f"'{self.body}' -{self.author}-"
