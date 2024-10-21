# Notebook for Plotly (Custom), Plotly Express (Quick), and Plotly Dash (Interactive Python Visualization Library)
# PRO: has hot loading, allowing quick realtime development both with new code and new data, React like
# CON: some small differences in allowed code between running in Jupyter Notebook and running in Dash app, but very minor

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, callback, html, Input, Output

# Load dataset
df = pd.read_csv('./data/fortune-500-01.csv', delimiter='\t')

# Peak at the data
df.head(5)

# Init dash app framework
app = Dash(name=__name__)

# Define dash app dashboard layout, two same graphs with different libraries: Plotly and Plotly Express
app.layout = html.Div([
    html.H1('Graph with Plotly', style={'color': 'white'}),
    dcc.Graph(id='output-graph-plotly'), # used in @callback( Output(...) )
    html.H1('Graph with Plotly Express', style={'color': 'white'}),
    dcc.Graph(id='output-graph-plotly-express'), # used in @callback( Output(...) )
    dcc.Dropdown(
        id='input-dropdown', # used in @callback( Input(...) )
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0]
    ),
])

# Define callback for Plotly graph
@callback(
    Output('output-graph-plotly', 'figure'),
    Input('input-dropdown', 'value')
)
def set_graph_plotly(input_dropdown):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df[input_dropdown], mode='lines+markers', name=input_dropdown))
    fig.update_layout(title='Fortune 500', xaxis_title='Year', yaxis_title=input_dropdown)
    # 🖤 easy on the eyes
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='rgba(255,255,255,255)')
    return fig

# Define callback for Plotly Express graph
@callback(
    Output('output-graph-plotly-express', 'figure'),
    Input('input-dropdown', 'value')
)
def set_graph_plotly_express(input_dropdown):
    fig = px.scatter(df, x=df.index, y=input_dropdown, title='Fortune 500', labels={'x': 'Year', 'y': input_dropdown})
    # 🖤 easy on the eyes
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='rgba(255,255,255,255)')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(port=8059, debug=True)
    
