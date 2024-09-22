import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real-Time Traffic Monitoring Dashboard"),
    dcc.Graph(id='live-update-graph'),
])

if __name__ == "__main__":
    app.run_server(debug=True)
