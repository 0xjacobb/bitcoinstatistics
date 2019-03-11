import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}

server = app.server

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='BITCOINSTATISTICS',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='A web application for interesting Bitcoin statistics', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div([
        html.Img(
            src='/assets/underConstruction.jpeg',
            style={
                'width': '20%'
            })
    ], style={'textAlign': 'center'})
])

if __name__ == '__main__':
    app.run_server(debug=True)