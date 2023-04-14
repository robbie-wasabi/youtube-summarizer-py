import requests
import re
from bs4 import BeautifulSoup
from config import Config

config = Config()


def is_valid_youtube_id(video_id):
    """Check if a YouTube video ID is valid"""
    regex = r"^[A-Za-z0-9_-]{11}$"
    return re.match(regex, video_id) is not None


def fetch_transcript(video_id):
    """Get the transcript of a YouTube video"""
    if not is_valid_youtube_id(video_id):
        return "Error: Invalid Youtube Video ID"

    url = config.youtext_url + video_id
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        return "Error: " + str(e)

    # Check if the response contains an HTTP error
    if response.status_code >= 400:
        return "Error: HTTP " + str(response.status_code) + " error"

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text
