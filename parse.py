from typing import Dict, List
import requests


def _showInfoUser(name_user) -> Dict:
    return requests.get(f'https://codeforces.com/api/user.info?handles={name_user}').json()['result'][0]

def _showRatingUser(name_user):
    return requests.get(f'https://codeforces.com/api/user.rating?handle={name_user}').json()['result']

def _showRatingList(start_pos: int,end_pos: int) -> List:
    rating = requests.get('https://codeforces.com/api/user.ratedList?activeOnly=true').json()['result'][start_pos:end_pos]
    for el in range(0,len(rating)):
        rating[el]['number_place'] = el + 1
    return rating
