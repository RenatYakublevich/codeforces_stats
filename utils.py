import requests


def _showInfoUser(name_user):
    return requests.get(f'https://codeforces.com/api/user.info?handles={name_user}').json()['result'][0]

print(_showInfoUser('tourist'))