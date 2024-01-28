# HKUST RVC videos bulk downloader
This project uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [Selenium](https://www.selenium.dev/) to download RVC videos from a list of URLs.

You probably need FFmpeg to be installed.

Supports videos from `rvcmedia.ust.hk` and `hkust.zoom.us` (planned, not implemented yet).
## Usage
### Setup virtual environment
```sh
python -m venv venv/ && source venv/bin/activate
```
### Install dependencies
```sh
pip install -r requirements.txt
```
### Edit configuration
Rename `.env.example` to `.env` and change accordingly.
### Run the damn script
include the file path of the links too
each video link should be seperated by new line
```sh
python main.py links.txt
```
