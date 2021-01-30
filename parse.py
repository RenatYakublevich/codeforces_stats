from typing import Dict
import requests


def _showInfoUser(name_user) -> Dict:
    return requests.get(f'https://codeforces.com/api/user.info?handles={name_user}').json()['result'][0]

def _showRatingUser(name_user):
    return requests.get(f'https://codeforces.com/api/user.rating?handle={name_user}').json()['result']

