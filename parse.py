''' Работа с API Codeforces '''
from typing import Dict, List
import requests


def _show_info_user(name_user: str) -> Dict:
    return requests.get(f'https://codeforces.com/api/user.info?handles={name_user}').json()['result'][0]

def _show_rating_user(name_user: str) -> Dict:
    return requests.get(f'https://codeforces.com/api/user.rating?handle={name_user}').json()['result']

def _show_rating_list(start_pos: int,end_pos: int) -> List:
    rating = requests.get('https://codeforces.com/api/user.ratedList?activeOnly=true').json()['result'][start_pos:end_pos]
    for number_place in range(0,len(rating)):
        rating[number_place]['number_place'] = number_place + 1
    return rating
  