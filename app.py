from pathlib import Path
import os
import random
import tempfile
from requests.packages import urllib3
import requests

from flask import Flask, render_template, request, redirect

from MemeEngine import MemeEngine
from QuoteEngine.model import QuoteModel
from QuoteEngine import Ingestor

app = Flask(__name__)

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get the current directory
current_dir = Path(__file__).parent

# Initialize the MemeEngine
meme = MemeEngine('./static')


def setup():
    """Setup loading all resources."""
    quotes_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                    './_data/DogQuotes/DogQuotesDOCX.docx',
                    './_data/DogQuotes/DogQuotesPDF.pdf',
                    './_data/DogQuotes/DogQuotesCSV.csv']

    # Parse the quotes from the quote files
    quotes = []
    quotes += Ingestor.parse_files(quotes_files)

    # Define the images directory to be used
    images_dir = "./_data/photos/dog/"

    # Get all the images in the images directory
    imgs = [os.path.join(images_dir, file) for file in os.listdir(images_dir) if file.endswith(".jpg")]

    return quotes, imgs


# Load all resources
quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""

    # Select a random image and quote using random.choice()
    img, quote = random.choice(imgs), random.choice(quotes)

    # Generate the meme and get the output path using a with statement
    out_path = meme.make_meme(img, quote)

    # Return the rendered meme template with the output path using f-strings
    return render_template('meme.html', path=f'{Path(out_path).relative_to(current_dir)}')


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme creation."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""

    try:
        # Get the image URL from the form data and download the image using requests.get()
        image_url = request.form.get("image_url")
        res = requests.get(image_url, verify=False)

        # Create a temporary file to write the image using tempfile.NamedTemporaryFile()
        with tempfile.NamedTemporaryFile(suffix='.png', dir=current_dir, delete=False) as tmp_f:
            tmp_f.write(res.content)

            # Get the body and author from the form data and create a QuoteModel object
            body = request.form.get("body")
            author = request.form.get("author")
            quote = QuoteModel(body, author)

            out_path = meme.make_meme(tmp_f.name, quote)

            # close the file and delete it
            os.remove(tmp_f.name)

        # Return the rendered meme template with the output path using f-strings
        return render_template('meme.html', path=f'{Path(out_path).relative_to(current_dir)}')

    except Exception as e:
        print(e)
        return redirect('/create')


if __name__ == "__main__":
    app.run()
