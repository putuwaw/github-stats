import requests
from math import ceil
from .utils import get_headers

BASE_URL = "https://api.github.com"


def get_name_total_repos(username: str) -> tuple:
    url = f'{BASE_URL}/users/{username}'
    try:
        response = requests.get(url, headers=get_headers())
        repos = response.json()['public_repos']
        name = response.json()['name']
        return name, repos
    except:
        raise Exception


def get_total_stars_earned(username: str, total_public_repos: int) -> int:
    per_page = 100
    page = 1
    limit = ceil(total_public_repos / per_page)
    query = f'?per_page={per_page}&page={page}'
    url = f'{BASE_URL}/users/{username}/repos'
    try:
        total_stars_earned = 0
        total_forks_earned = 0
        while page <= limit:
            response = requests.get(url+query, headers=get_headers())
            for repo in response.json():
                total_stars_earned += repo['stargazers_count']
                total_forks_earned += repo['forks_count']
            page += 1
        return total_stars_earned, total_forks_earned
    except:
        raise Exception


def get_total_merged_pr(username: str) -> int:
    url = f'{BASE_URL}/search/issues'
    query = f'?q=author:{username}+is:merged'
    try:
        response = requests.get(url+query, headers=get_headers())
        result = response.json()['total_count']
        return result
    except:
        raise Exception


def get_total_commits(username: str) -> int:
    url = f'{BASE_URL}/search/commits'
    query = f'?q=author:{username}'
    try:
        response = requests.get(url+query, headers=get_headers())
        result = response.json()['total_count']
        return result
    except:
        raise Exception
