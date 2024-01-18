# HKUST RVC videos bulk downloader
This project uses yt-dlp and Selenium to download RVC videos from a list of URLs.

You need Google Chrome or Mozilla Firefox to be installed on your computer, oh and FFmpeg too.
## Usage
### Setup virtual environment
```sh
python -m venv venv/ && source venv/bin/activate
```
### Install dependencies
```sh
pip install -r requirements.txt
```
### Run the damn script
include the file path of the links too
```sh
python main.py links.txt
```
You will be asked to login with your ITSC account, please do it :), then the program will handle the rest