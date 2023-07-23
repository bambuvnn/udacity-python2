from Exceptions import InvalidFilePathException
from PIL import Image, ImageFont, ImageDraw
import random
import tempfile
import os


class MemeEngine:
    """MemeEngine class to generate meme."""
    default_font = "./_data/font/Ruluko-Regular.ttf"
    default_font_size = 20

    def __init__(self, output_dir):
        """Initialize MemeEngine with given path."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def make_meme(self, img_path, quote, width=500, font_size=default_font_size) -> str:
        """Make meme with given img_path, text, author and width."""
        width = min(width, 500)

        _, out_path = tempfile.mkstemp(
            dir=self.output_dir, prefix="meme-", suffix=".png")

        quote_str = str(quote)

        try:
            with Image.open(img_path) as img:
                if img.width > width:
                    height = int(img.height * width / img.width)
                    outputImg = img.resize((width, height))
                else:
                    outputImg = img

                draw = ImageDraw.Draw(outputImg)
                font = ImageFont.truetype(
                    self.default_font, font_size)

                coor_x = random.randint(0, int(img.width/4))
                coor_y = random.randint(0, int(img.height/4))

                draw.text((coor_x, coor_y), quote_str,
                          font=font, fill=(255, 0, 0))

                outputImg.save(out_path)

        except Exception:
            raise InvalidFilePathException("Invalid img file path")

        return out_path
