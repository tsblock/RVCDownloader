# HKUST RVC videos bulk downloader
This project uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [Selenium](https://www.selenium.dev/) to download RVC videos from a list of URLs.

You probably need FFmpeg to be installed.

Supports videos from `rvcmedia.ust.hk` and `hkust.zoom.us`.
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
You will be asked to login with your ITSC account, please do it :), then the program will handle the rest.