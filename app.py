import os

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd

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
            value=5,
            max=10,
            min=0,
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
                'fontWeight' : 'bold'
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

if __name__ == '__main__':
    app.run_server(debug=True)
