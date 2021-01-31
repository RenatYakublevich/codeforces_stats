from datetime import datetime
from flask import Flask, render_template, url_for
from parse import _showInfoUser, _showRatingUser, _showRatingList
from charts import _route_charts


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',title='Главная')

@app.route('/<path:name>')
def showInfoUser(name):
    try:
        stats = _showInfoUser(name)
    except KeyError:
        return render_template('info_user.html',stats=['Такого пользователя нет!'])

    script,div,js_resources,css_resources = _route_charts(_showRatingUser(name))

    return render_template('info_user.html',stats=[f'Никнейм - {stats["handle"]}',
                                                   f'Имя - {stats["firstName"]}',
                                                   f'Фамилия - {stats["lastName"]}',
                                                   f'Рейтинг - {stats["rating"]}',
                                                   f'Максимальный рейтинг - {stats["maxRating"]}',
                                                   f'Ранг - {stats["rank"]}',
                                                   f'Максимальный ранг - {stats["maxRank"]}',
                                                   f'Страна - {stats["country"]}',
                                                   f'Город - {stats["city"]}',
                                                   f'Последний раз заходил - {datetime.utcfromtimestamp(stats["lastOnlineTimeSeconds"]).strftime("%Y-%m-%d %H:%M:%S")}',
                                                   f'Зарегистрировался - {datetime.utcfromtimestamp(stats["registrationTimeSeconds"]).strftime("%Y-%m-%d %H:%M:%S")}',
                                                   f'Организация - {stats["organization"]}'
                                                   ],
                                            photo=stats['titlePhoto'],
                                            plot_script=script,
                                            plot_div=div,
                                            js_resources=js_resources,
                                            css_resources=css_resources,
                           )

@app.route('/rating')
def rating():
    return render_template('rating.html',rating=_showRatingList(0,20))

if __name__ == '__main__':
    app.run(debug=True)