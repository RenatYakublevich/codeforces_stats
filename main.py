from datetime import datetime
from flask import Flask, render_template, url_for
from parse import _show_info_user, _show_rating_user, _show_rating_list, _show_problem_list, _show_tournament_list, _show_user_submission, _show_user_blog, _show_history_tournament, _show_tournament_info, _show_problems_info
from charts import _route_charts


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',title='Главная')

@app.route('/<path:name>')
def showInfoUser(name):
    try:
        stats = _show_info_user(name)
    except KeyError:
        return render_template('error.html',error_msg='Такого пользователя нет!')

    script,div,js_resources,css_resources = _route_charts(_show_rating_user(name))

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
                                            title=stats['handle']
                           )

@app.route('/rating')
def rating():
    return render_template('rating.html',rating=_show_rating_list(0,20),title='Рейтинг')

@app.route('/problems')
def problems():
    return render_template('problems.html',problems=_show_problem_list(0,20),title='Задачи')

@app.route('/tournaments')
def tournaments():
	return render_template('tournaments.html', tournaments=_show_tournament_list())

@app.route('/<path:name>/submissions/<int:start>/')
def get_status(name, start):
    try:
        return render_template('submission.html', submissions=_show_user_submission(name,start * 10,10),page_prev=start - 1, page_next= start + 1, name= name)
    except KeyError:
        return render_template('error.html',error_msg='Такой страницы нет!')

@app.route('/<path:name>/blog')
def get_blog(name):
    return render_template('blog.html', blog=_show_user_blog(name))

@app.route('/history_tournaments')
def get_history_tournaments():
    return render_template('history_tournaments.html', tournaments=_show_history_tournament())

@app.route('/tournament/<path:id_tournament>')
def get_tournament_info(id_tournament):
    return render_template('tournament_info.html', tournament=_show_tournament_info(id_tournament), problems=_show_problems_info(id_tournament), id_tournament=id_tournament)

if __name__ == '__main__':
    app.run(debug=True)