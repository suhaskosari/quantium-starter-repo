import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the processed data
df = pd.read_csv('data/output.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

app = dash.Dash(__name__)

app.layout = html.Div(style={
    'backgroundColor': '#1a1a2e',
    'minHeight': '100vh',
    'fontFamily': 'Arial, sans-serif',
    'padding': '20px'
}, children=[

    html.H1('Pink Morsel Sales Visualiser', style={
        'textAlign': 'center',
        'color': '#e94560',
        'fontSize': '2.5em',
        'marginBottom': '10px',
        'letterSpacing': '2px'
    }),

    html.P('Analyse Pink Morsel sales before and after the price increase on Jan 15, 2021', style={
        'textAlign': 'center',
        'color': '#a8a8b3',
        'marginBottom': '30px'
    }),

    html.Div(style={
        'textAlign': 'center',
        'marginBottom': '20px'
    }, children=[
        html.Label('Filter by Region:', style={
            'color': '#e94560',
            'fontWeight': 'bold',
            'marginRight': '15px',
            'fontSize': '1.1em'
        }),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' All', 'value': 'all'},
                {'label': ' North', 'value': 'north'},
                {'label': ' South', 'value': 'south'},
                {'label': ' East', 'value': 'east'},
                {'label': ' West', 'value': 'west'},
            ],
            value='all',
            inline=True,
            style={'color': '#ffffff'},
            labelStyle={
                'marginRight': '20px',
                'fontSize': '1em',
                'cursor': 'pointer'
            }
        )
    ]),

    html.Div(style={
        'backgroundColor': '#16213e',
        'borderRadius': '15px',
        'padding': '20px',
        'boxShadow': '0 4px 20px rgba(233, 69, 96, 0.3)'
    }, children=[
        dcc.Graph(id='sales-chart')
    ])
])

@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x='date', y='sales', color='region',
                  title='Pink Morsel Sales Over Time',
                  labels={'date': 'Date', 'sales': 'Sales ($)'})

    fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000,
                  line_dash='dash', line_color='#e94560',
                  annotation_text='Price Increase')

    fig.update_layout(
        plot_bgcolor='#1a1a2e',
        paper_bgcolor='#16213e',
        font_color='#ffffff',
        title_font_color='#e94560',
        legend=dict(bgcolor='#1a1a2e', bordercolor='#e94560', borderwidth=1)
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)