import httpx
from .utils import get_headers

BASE_URL = "https://api.github.com/graphql"


def get_name_total_repos(username: str) -> tuple:
    query = '''
    query GetNameTotalRepos {
        user(login: "%s") {
            name
            repositories(first: 1, privacy: PUBLIC) {
                totalCount
            }
        }
    }
    ''' % username

    payload = {
        'query': query
    }

    response = httpx.post(BASE_URL, json=payload, headers=get_headers())
    if response.status_code == 200:
        data = response.json()
        name = data['data']['user']['name']
        repos = data['data']['user']['repositories']['totalCount']
        return name, repos
    else:
        raise Exception


def get_total_stars_earned(username: str) -> tuple:
    hasNextPage = True
    totalStars = 0
    totalForks = 0
    after = ""

    while (hasNextPage):
        query = '''
        query GetTotalStarsEarned {
            user(login: "%s"){
                repositories(first: 100, privacy: PUBLIC, %s){
                    nodes{
                        stargazerCount
                        forkCount
                    }
                    pageInfo{
                        endCursor
                        hasNextPage
                    }
                }
            }
        }
        ''' % (username, after)

        payload = {
            'query': query
        }

        response = httpx.post(BASE_URL, json=payload, headers=get_headers())
        if response.status_code == 200:
            data = response.json()['data']['user']['repositories']

            stars = sum(repo['stargazerCount'] for repo in data['nodes'])
            forks = sum(repo['forkCount'] for repo in data['nodes'])
            totalStars += stars
            totalForks += forks

            hasNextPage = data['pageInfo']['hasNextPage']
            endCursor = data['pageInfo']['endCursor']
            after = f'after: "{endCursor}"'
        else:
            raise Exception

    return totalStars, totalForks


def get_total_merged_pr(username: str) -> int:
    query = '''
    query GetTotalMergedPR{
        search(query: "type:pr is:merged author:%s", type: ISSUE, first: 1) {
            issueCount
        }   
    }
    ''' % username

    payload = {
        'query': query
    }

    response = httpx.post(BASE_URL, json=payload, headers=get_headers())
    if response.status_code == 200:
        data = response.json()
        result = data['data']['search']['issueCount']
        return result
    else:
        raise Exception


def get_total_commits(username: str) -> int:
    query = '''
    query GetTotalCommits{
        user(login: "%s") {
            contributionsCollection {
                totalCommitContributions
            }
        }
    }
    ''' % username

    payload = {
        'query': query
    }

    response = httpx.post(BASE_URL, json=payload, headers=get_headers())
    if response.status_code == 200:
        data = response.json()
        result = data['data']['user']['contributionsCollection']['totalCommitContributions']
        return result
    else:
        raise Exception
