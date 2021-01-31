from datetime import datetime
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE


def _create_bar_chart(x,top):
    """
    Создаёт столбчатую диаграмму
    """
    fig = figure(plot_width=1100, plot_height=600)
    fig.vbar(
        x=x,
        width=0.5,
        bottom=0,
        top=top,
        color='navy'
    )

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(fig)
    return script, div, js_resources, css_resources

def _route_charts(rating_data):
    """
    Собирает
    :param rating_data: словарь с данными пользователя из API
    :return: script, div, js_resources, css_resources
    """
    data_charts = {
        'oldRating': [info['oldRating'] for info in rating_data],
        'newRating': [info['newRating'] for info in rating_data],
        'contestName': [info['contestName'] for info in rating_data],
        'rank': [info['rank'] for info in rating_data],
        'ratingUpdateTimeSeconds': [int(datetime.utcfromtimestamp(info['ratingUpdateTimeSeconds']).strftime("%Y")) for info in rating_data]
    }

    plot = _create_bar_chart(data_charts['ratingUpdateTimeSeconds'],data_charts['newRating'])

    return plot


