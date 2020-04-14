import json
import plotly.graph_objects as go
import plotly.offline as po
import pandas as pd
import math
import numpy as np
import datetime


def plot_time_series(array, time):
    data = [go.Scatter(
        x=np.array(time),
        y=array,
        text=['累计账户金额:{}'.format(num) for num in array],
        mode='lines+markers',
        marker=dict(
                    size=12,
                    color=[num if not math.isnan(num) else 0 for num in array],
                    colorscale='Viridis',
                    showscale=True),
        line=dict(width=3, color='lightseagreen')
    )]
    layout = go.Layout(
        height=350,
        margin={'l': 20, 'b': 30, 'r': 20, 't': 10},
        xaxis={'title': '日期', 'showgrid': False},
        yaxis={'title': '累计账户金额'},
        paper_bgcolor='#E2E9FF',
        plot_bgcolor='#E5EBF7',
        hovermode='closest'
    )
    fig = go.Figure(
        data=data,
        layout=layout,
    )
    return fig