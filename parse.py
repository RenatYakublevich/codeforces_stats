''' Работа с API Codeforces '''
from typing import Dict, List
from datetime import datetime
import requests


def _show_info_user(name_user: str) -> Dict:
	"""
	Функция возвращает словарь информации о пользователе по его хендлеру(name_user)
	"""
	return requests.get(f'https://codeforces.com/api/user.info?handles={name_user}').json()['result'][0]

def _show_rating_user(name_user: str) -> Dict:
	"""
	Функция возвращает словарь изменений рейтинга пользователя по его хендлеру(name_user)
	"""
	return requests.get(f'https://codeforces.com/api/user.rating?handle={name_user}').json()['result']

def _show_rating_list(start_pos: int,end_pos: int) -> List:
	"""
	Функция возвращает список топа рейтинга, со срезом start_pos:end_pos
	"""
	return requests.get('https://codeforces.com/api/user.ratedList?activeOnly=true').json()['result'][start_pos:end_pos]

def _show_problem_list(start_pos: int, end_pos: int) -> List:
	"""
	Функция возвращает список задач со срезом start_pos:end_pos
	"""
	return requests.get('https://codeforces.com/api/problemset.problems').json()['result']['problems'][start_pos:end_pos]

def _show_tournament_list() -> List:
	"""
	Функция возвращает список предстоящих турниров
	"""
	tournaments = []
	for tournament in requests.get('https://codeforces.com/api/contest.list?gym=false').json()['result']:
		if tournament['phase'] != 'BEFORE':
			break
		tournaments.append(tournament)
	for tournament in range(len(tournaments)):
		tournaments[tournament]['durationSeconds'] = datetime.utcfromtimestamp(tournaments[tournament]['durationSeconds']).strftime("%H:%M:%S")
		tournaments[tournament]['startTimeSeconds'] = datetime.utcfromtimestamp(tournaments[tournament]['startTimeSeconds']).strftime("%d.%m.%Y %H:%M:%S")

	return tournaments

def _show_user_submission(name_user: str, start_pos: int, end_pos: int) -> List:
	"""
	Функция возвращает попытки пользователя по его хендлеру(name_user) со срезом start_pos:end_pos
	"""
	if start_pos == 0:
		start_pos = 1
	submissions = requests.get(f'https://codeforces.com/api/user.status?handle={name_user}&from={start_pos}&count={end_pos}').json()['result']
	for submission in range(len(submissions)):
		submissions[submission]['creationTimeSeconds'] = datetime.utcfromtimestamp(submissions[submission]['creationTimeSeconds']).strftime("%d.%m.%Y %H:%M:%S")
	return submissions

def _show_user_blog(name_user: str) -> List:
	"""
	Функция возвращает записи в блоге пользователя по его хендлеру(name_user)
	"""
	return requests.get(f'https://codeforces.com/api/user.blogEntries?handle={name_user}').json()['result']

def _show_history_tournament() -> List:
	"""
	Функция возвращает список истории турниров
	"""
	request = requests.get('https://codeforces.com/api/contest.list?gym=false').json()['result']
	indent = 0

	for tournament in request:
		if tournament['phase'] != 'BEFORE':
			break
		indent += 1
	return request[indent::]

def _show_tournament_info(id_tournament: int) -> Dict:
	"""
	Функция возвращает словарь информации о турнире по его id(id_tournament)
	"""
	request = requests.get(f'https://codeforces.com/api/contest.standings?contestId={id_tournament}&from=1&count=5&showUnofficial=true').json()['result']['contest']
	request['durationSeconds'] = datetime.utcfromtimestamp(request['durationSeconds']).strftime("%H:%M:%S")
	request['startTimeSeconds'] = datetime.utcfromtimestamp(request['startTimeSeconds']).strftime("%d.%m.%Y %H:%M:%S")
	return request

def _show_problems_info(id_tournament: int) -> List:
	"""
	Функция возвращает информацию о задачах турнира по его id(id_tournament)
	"""
	return requests.get(f'https://codeforces.com/api/contest.standings?contestId=1477&from=1&count=5&showUnofficial=true').json()['result']['problems']