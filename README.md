## Data Dashboard in Python
django, plotly dash, matplotlib

## Python Web Framework
- Django

## Python Data Visualization 
### Plotly Dash (dynamic, interactive, dashboard)
- Plotly Dash is built on top of:
	- Plotly (`go` for custom graphs)
	- Plotly Express (`px` for quick graphs)
	- React (for interactive part of updating graphs)
- Plotly Dash is used for creating interactive data visualizations
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