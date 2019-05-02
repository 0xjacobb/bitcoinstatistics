import os

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd
from dash.dependencies import Input, Output

import twitter_streamer

hash_tag_list = ["bitcoin", ]
streamer = twitter_streamer.TwitterStreamer()
twitter_streamer.stream_tweets(hash_tag_list)

# reading data for statistic table
df = pd.read_csv('data.csv')

app = dash.Dash(__name__)

# needed because of Heroku deployement https://github.com/plotly/dash-daq/issues/25
app.scripts.config.serve_locally = True

colors = {
    'background': '#323232',
    'background_dark': '#1e1e1e',
    'text': '#FFFFFF'
}

server = app.server

app.layout = html.Div([

    html.Div([
        html.H1('BITCOIN HEATMETER'),
    ], className='row', style={'textAlign': 'center'}),

    html.Div([
        html.Label('How interesting is Bitcoin to the world?'),
    ], style={'textAlign': 'center'}),

    dcc.Interval(
        id='interval-component',
        interval=1*10000,  # in milliseconds
        n_intervals=0
    ),

    # https://dash.plot.ly/dash-daq/gauge
    html.Div([
        daq.Gauge(
            id='bitcoin-gauge-chart',
            value=2,
            max=10,
            min=0,
            units="MPH",
            color={"gradient": True, "ranges": {
                "green": [0, 6], "yellow": [6, 8], "red": [8, 10]}},
        )
    ], className='row', style={'textAlign': 'center'}),

    html.Div([
        html.Label('24h interest since 2019-04-01'),
    ], className='row', style={'textAlign': 'center'}),

    html.Div([
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("rows"),
            style_header={
                'backgroundColor': colors['background_dark'],
                'fontWeight': 'bold'
            },
            style_cell={
                'backgroundColor': colors['background'],
                'color': 'white',
                'minWidth': '30px', 'width': '50px', 'maxWidth': '90px'
            },
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'center'
                } for c in df.columns
            ],
        )
    ], className='row four columns offset-by-four'),

    html.Div([
        html.Label('Donate: BTC address'),
        html.Img(
            src='/assets/qrcode.png',
            style={'width': '120px'}
        )
    ], className='row', style={'textAlign': 'center'}),

], style={'backgroundColor': colors['background'], 'color': colors['text']})

# takes value from id='test_input' and return the value in value of id='bitcoin-gauge-chart'
@app.callback([
    Output('bitcoin-gauge-chart', 'value'),
    Output('bitcoin-gauge-chart', 'max'),
    Output('bitcoin-gauge-chart', 'color'),
],  [Input('interval-component', 'n_intervals'), ]
)
def update_gauge(n_intervals):
    max = 100
    min = 0
    value = twitter_streamer.get_number_of_tweets()
    print("TWEETS: ", value)
    threshold_1 = max-round(max*0.6)
    threshold_2 = max-round(max*0.3)

    color = {"gradient": True, "ranges": {
        "green": [min, threshold_1], "yellow": [threshold_1, threshold_2], "red": [threshold_2, max]}}
    return value, max, color


if __name__ == '__main__':
    app.run_server(debug=True)
