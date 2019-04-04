import os

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
'''
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    '''

data = (
    [
        ("Date", ["2015-01-01", "2015-10-24"]),
        ("Tweets", [100, 1000]),
        ("Google", [900, 3500]),
    ]
),

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# needed because of Heroku deployement https://github.com/plotly/dash-daq/issues/25
app.scripts.config.serve_locally = True

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

server = app.server

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='BITCOIN HEATMETER',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='How interesting is Bitcoin to the world?', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div([
        html.Img(
            src='/assets/underConstruction.jpeg',
            style={
                'width': '10%'
            })
    ], style={'textAlign': 'center'}),

    # https://dash.plot.ly/dash-daq/gauge
    html.Div([
        daq.Gauge(
            id='bitcoin-gauge-chart',
            color={"gradient": True, "ranges": {
                "green": [0, 6], "yellow":[6, 8], "red":[8, 10]}},
            size=300,
            label="",
            showCurrentValue=True,
            units="MPH",
            value=6,
            max=10,
            min=0,
        )
    ], style={'textAlign': 'center'}),

    html.Div(children='24h interest since 2019-04-01',
             style={
                 'textAlign': 'center',
                 'color': colors['text']
             }
             ),

    # https://dash.plot.ly/datatable
    html.Div([
        dash_table.DataTable(
            id='table',
            # columns=[{"name": i, "id": i} for i in df.columns],
            # data=df.to_dict("rows"),
            # df=pd.DataFrame(data)
            columns=[{"name": i, "id": i} for i in data],
        )
    ], style={'textAlign': 'center'}),
])

if __name__ == '__main__':
    app.run_server(debug=True)
