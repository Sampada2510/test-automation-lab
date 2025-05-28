# Required Libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load Data
df = pd.read_csv("user_sessions.csv", parse_dates=['timestamp'])

# Data Cleanup
df = df.dropna(subset=['feature_name', 'event_type', 'timestamp', 'Place'])

# Filter drop events
drop_df = df[df['event_type'] == 'drop']

# Initialize Dash App
app = Dash(__name__)
app.title = "User Drop-Off Analytics Dashboard"

# Layout
app.layout = html.Div([
    html.H1("User Session Analytics Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Filter by Device Type:"),
        dcc.Dropdown(
            id='device-dropdown',
            options=[{'label': d, 'value': d} for d in df['device_type'].unique()],
            value=df['device_type'].unique()[0],
            clearable=False
        )
    ], style={'width': '40%', 'margin': 'auto'}),

    dcc.Graph(id='drop-chart'),

    html.Div([
        html.H4("Raw Drop-Off Data Sample"),
        html.Div(id='table-sample')
    ], style={'padding': '20px'})
])

# Callbacks
@app.callback(
    [Output('drop-chart', 'figure'),
     Output('table-sample', 'children')],
    [Input('device-dropdown', 'value')]
)
def update_dashboard(selected_device):
    filtered = drop_df[drop_df['device_type'] == selected_device]
    drop_summary = filtered['feature_name'].value_counts().reset_index()
    drop_summary.columns = ['feature_name', 'drop_count']

    fig = px.bar(
        drop_summary, x='feature_name', y='drop_count',
        title=f"Drop-Offs by Feature ({selected_device})",
        labels={'drop_count': 'Number of Drop-offs', 'feature_name': 'Feature'},
        color='feature_name'
    )

    table_html = filtered[['user_id', 'session_id', 'feature_name', 'timestamp', 'Place']].head(10).to_html(index=False)

    return fig, html.Div([dcc.Markdown("##### Sample Drop Events"), html.Div(table_html, style={'overflowX': 'scroll'})])

# Run Server
if __name__ == '__main__':
    app.run(debug=True)