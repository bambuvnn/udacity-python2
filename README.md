# Meme Generator

This is a meme generator that can either be used as a web app or a CLI. It allows users to create memes with their own images and captions.

## How to Install

To install the necessary dependencies, run the following command:

```sh
$ pip install -r requirements.txt
```

## How to Use

### CLI

To create a meme via the command line interface, run the following command:

```sh
$ python meme.py
```

The generated meme will be saved in the `tmp` folder.

### Web App

To create a meme via the web app, run the following command:

```sh
$ python app.py
```

Then, open your web browser and go to `http://127.0.0.1:5000`. You can now upload an image and add your desired captions. The generated meme will be saved in the `static` folder.

## Requirements

- Python 3.x
- Flask
- Pillow

See `requirements.txt` for more information.