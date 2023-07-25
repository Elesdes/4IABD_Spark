import os

import dash
import pandas as pd
import plotly.graph_objects as go
from dash import dcc, html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots


def file_csv(folder):
    """
    This function takes in a directory as input.
    It returns the latest CSV file from the specified directory.
    """
    files = os.listdir(folder)
    for file in files:
        if file.endswith('.csv'):
            return file


name_file = (file_csv(
    r"C:\Users\sofia\Desktop\4iabd\sparkStreamingScala\src\main\ressources\all_files_spark\group_by_days_hour_sport"))
df = pd.read_csv(
    r"C:\Users\sofia\Desktop\4iabd\sparkStreamingScala\src\main\ressources\all_files_spark\group_by_days_hour_sport\\" + name_file)
df["TS"] = pd.to_datetime(df["date"] + df["hour"].astype(str), format="%Y-%m-%d%H")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.DatePickerSingle(
        id='date-picker',
        min_date_allowed=df['TS'].min(),
        max_date_allowed=df['TS'].max(),
        initial_visible_month=df['TS'].min(),
        date=df['TS'].min()
    ),
    dcc.Graph(id='output-graph')
])


@app.callback(
    Output('output-graph', 'figure'),
    [Input('date-picker', 'date')])
def update_output(date):
    df2 = df[df.date == date]

    fig = make_subplots(rows=1, cols=1)

    fig.add_trace(go.Scatter(x=df2["hour"], y=df2["avg_value"], mode='lines+markers', name='Average Value',
                             line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df2["hour"], y=df2["min_value"], mode='lines+markers', name='Min Value',
                             line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df2["hour"], y=df2["max_value"], mode='lines+markers', name='Max Value',
                             line=dict(color='red')))
    fig.update_layout(height=600, title_text="Values by Hour for Date: " + date)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
