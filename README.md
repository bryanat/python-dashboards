## Data Dashboard in Python
django, plotly dash, matplotlib

## Python Data Visualization 
### Plotly Dash (dynamic, realtime, interactive, dashboard)
- Plotly Dash is used for creating interactive data visualizations.
- Plotly Dash is built on top of:
	- Plotly (`go` for custom graphs)
	- Plotly Express (`px` for quick graphs)
	- React (for interactive part of updating graphs)
- Plotly Dash technical understanding:
	- `@callback()` controls IO (via a function decorator)
		- `@callback( Input(...) )` 
			- `@callback( Input('input-xx', 'value') )` 
		- `@callback( Output(...) )` 
			- `@callback( Output('output-xx', 'figure') )` 
		- `@callback() def function_to_update_graph( input_var_basically_passed_from_input-xx )`
	- `app.layout` holds layout of all frontend components (displays, graphs, interactables)
		- `id`s from `dcc` & `html` components in `app.layout` are used in `@callback(Input(...))` and `@callback(Output(...))`
		- minor detail but `app.layout` needs a top level div for Jupyter Notebooks, so make it a standard even in app.py
			- `app.layout = dash.html.Div([...])`
	```python
	import dash
	app.layout = dash.html.Div([
		# Graph is really just a placeholder component, filled by figure function below
		dash.dcc.Graph(id='output-figure', ...),
		dash.dcc.Dropdown(id='input-value', ...)
	])
	@callback(
		Output('output-figure', 'figure'),
		Input('input-value', 'value')
	)
	def update_figure(input_value):
		# px (quick) or go (custom) figure
		figure = px.line(df, x=df.index, y=input_value)
		return figure
	```

### Matplotlib (static, report)
- Matplotlib 

## Python Web Framework
- Django
- Django MTV
	- M: Django's Model is pulling data from FastAPI : data model, Object-relational mapper https://docs.djangoproject.com/en/5.1/topics/db/models/
	- T: Django's Template is rendering our Plotly Dash templates: `{ handlebars }` holding `app.layout(...)` https://docs.djangoproject.com/en/5.1/topics/templates/
	- V: Django's View is routes and input determining what Templates customers will see : URLs and Views `path('xx/')` https://docs.djangoproject.com/en/5.1/topics/http/urls/
		- would we pass user input into dash's callback as input: `@callback( Input(...) )`
	- Realtime: Plotly Dash is for visualizing interactive charts that update in **realtime**, like a monitoring dashboard
		- so we can make sure machines are operating correctly in realtime
		- with plotly dash we can interact with the dashboard's charts for further information why certain metrics are at the state they're in
		- Timeseries data from Machines
			- uptime, downtime is important, data modeled as timeseries data
			- moving averages, windows, rate changes +x% -x%
		- Django (M & V) will serve this data, and Django's Template (T) will act like a shell holding Plotly Dash figures  
- Django ORM (M)