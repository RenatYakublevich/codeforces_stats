# codeforces_stats
Codeforces Stats - сайт со статистикой Codeforces

Статистика берётся с оффициального `API Codeforces`

Стек технологий:
 - Микрофреймворк `Flask`
 - библиотека для работы с HTTP запросами `aiohttp`
 - библиотека для построения графиков `bokeh`

Архитектура проекта:
  - main.py - основной файл, где происходит работа с `Flask`
  - parse.py - файл, где находятся функции для работы с `Codeforces API`
  - charts.py - файл, где происходит работа с графиками
  - templates/... - html файлы вёрстки, `base.html` - html родитель
 
