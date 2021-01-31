''' Работа с API Codeforces '''
from typing import Dict, List
from datetime import datetime
import requests


def _show_info_user(name_user: str) -> Dict:
    return requests.get(f'https://codeforces.com/api/user.info?handles={name_user}').json()['result'][0]

def _show_rating_user(name_user: str) -> Dict:
    return requests.get(f'https://codeforces.com/api/user.rating?handle={name_user}').json()['result']

def _show_rating_list(start_pos: int,end_pos: int) -> List:
    rating = requests.get('https://codeforces.com/api/user.ratedList?activeOnly=true').json()['result'][start_pos:end_pos]
    for number_place,rate in enumerate(rating):
        rating[number_place]['number_place'] = number_place + 1
    return rating

def _show_problem_list(start_pos: int, end_pos: int) -> List:
    return requests.get('https://codeforces.com/api/problemset.problems').json()['result']['problems'][start_pos:end_pos]

def _show_tournament_list() -> List:
	tournaments = []
	for tournament in requests.get('https://codeforces.com/api/contest.list?gym=false').json()['result']:
		if tournament['phase'] != 'BEFORE':
			break
		tournaments.append(tournament)
	for tournament in range(len(tournaments)):
		tournaments[tournament]['durationSeconds'] = datetime.utcfromtimestamp(tournaments[tournament]['durationSeconds']).strftime("%H:%M:%S")
		tournaments[tournament]['startTimeSeconds'] = datetime.utcfromtimestamp(tournaments[tournament]['startTimeSeconds']).strftime("%d.%m.%Y %H:%M:%S")

	return tournaments