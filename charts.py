from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.models.sources import ColumnDataSource


def create_hover_tool():
    return None

def create_bar_chart(x,top):
    """
    Создаёт столбчатую диаграмму.
    Принимает данные в виде словаря, подпись для графика,
    названия осей и шаблон подсказки при наведении.
    """
    fig = figure(plot_width=600, plot_height=600)
    fig.vbar(
        x=x,
        width=0.5,
        bottom=0,
        top=top,
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    return script, div, js_resources, css_resources

def route_charts(rating_data):
    data_charts = {
        'id': tuple([c for c in range(1,len(rating_data) + 1)]),
        'oldRating': [],
        'newRating': [],
        'contestName': [],
        'rank': []
    }
    for count,bar in enumerate(rating_data):
        data_charts['oldRating'].append(bar['oldRating'])
        data_charts['newRating'].append(bar['newRating'])
        data_charts['contestName'].append(bar['contestName'])
        data_charts['rank'].append(bar['rank'])
    hover = create_hover_tool()
    plot = create_bar_chart(data_charts['oldRating'],data_charts['newRating'])

    return plot


