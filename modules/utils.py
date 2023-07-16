from dotenv import load_dotenv
import os

load_dotenv()


def get_headers():
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    HEADERS = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer " + GITHUB_TOKEN,
        "X-GitHub-Api-Version": "2022-11-28"
    }
    return HEADERS
