# WORK IN PROGRESS: script not working yet
# HKUST RVC videos bulk downloader
This project uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [Selenium](https://www.selenium.dev/) to download RVC videos from a list of URLs.

You probably need FFmpeg to be installed.

Supports videos from `rvcmedia.ust.hk`, more sites will be supported.
# Usage
## Setup virtual environment
```sh
python -m venv venv/ && source venv/bin/activate
```
## Install dependencies
```sh
pip install -r requirements.txt
```
## Edit configuration
Rename `.env.example` to `.env` and change accordingly.
## Run the script
include the file path of the links

each video link should be seperated by new line
```sh
python main.py links.txt
```
You will be asked to login, do that, also when getting through 2FA select remember my device.

# Q&A
## Why?
1. Mostly for archival purposes, HKUST deletes RVC videos after its respecive semester has ended.
2. Navigating Canvas just to get recordings is annoying, I'm lazy ok?
3. eduroam in HKUST is slow, let me download all the stuff at home so I don't need to wait when I'm in campus

## Why use selenium? Using a whole browser just to download some videos seems unnecessary
That's true, unfortunately I'm lazy and don't want to figure out how to properly interact with HKUST's SSO service.
## GUI when?
This project was originally created for personal use, if there's a demand then maybe I will add a GUI. However, I would much prefer if someone else work on it because I have 0 experience on making GUI app. 


