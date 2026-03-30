import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the processed data
df = pd.read_csv('data/output.csv')

# Sort by date
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Create the line chart
fig = px.line(df, x='date', y='sales', color='region',
              title='Pink Morsel Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales ($)'})

# Add a vertical line for the price increase date
fig.add_vline(x=pd.Timestamp('2021-01-15').timestamp() * 1000,
              line_dash='dash', line_color='red',
              annotation_text='Price Increase')

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Pink Morsel Sales Visualiser',
            style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)