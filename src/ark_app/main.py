"""Module for the main entrypoint to the application"""
__all__ = ["main"]

import dash
from dash import dcc
from dash import html
import os

dash_app = dash.Dash(__name__, use_pages=True)

#Creates Dash App Layout
dash_app.layout = html.Div([
    html.H1('Graph Dashboard'),
    html.Div([
        html.Div(
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

def main():
    dash_app.run_server(debug=True, host='0.0.0.0', port=8000)
