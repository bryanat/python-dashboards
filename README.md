## Data Dashboard in Python
django, plotly dash, matplotlib

## Python Data Visualization
- Plotly Dash (interactive): Plotly `go` (low-level, interactive) & Plotly Express `px` (high-level, interactive)
- Pandas Reports (static): Matplotlib `plt` (low-level, static) & Seaborn `sns` (high-level, static)
### Plotly Dash (dynamic, realtime, interactive, dashboard)
- Plotly Dash `dash` is used for creating interactive data visualizations.
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
- Matplotlib `plt` & Seaborn `sns`
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-01-mle-basictools/pandas-sklearn-basics/pandas-sklearn-basics.ipynb
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-08-unsupervised-ml/LiveDemo/dimensionality-reduction-pca-and-tsne.ipynb
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-08-unsupervised-ml/LiveDemo/popular-unsupervised-clustering-algorithms.ipynb
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-04-data-eng-airflow/nb/walmart-sales-data.ipynb
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-04-data-eng-airflow/demos/house-prices-advanced-regression-techniques.ipynb
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-08-unsupervised-ml/nb/new-product-launch.ipynb


## Python Web Framework
### Django
- Django MVT
	- M: Django's Model is pulling data from FastAPI : data model, Object-relational mapper https://docs.djangoproject.com/en/5.1/topics/db/models/
	- V: Django's View is routes and input determining what Templates customers will see : URLs and Views `path('xx/')` https://docs.djangoproject.com/en/5.1/topics/http/urls/
		- would we pass user input into dash's callback as input: `@callback( Input(...) )`
	- T: Django's Template is rendering our Plotly Dash templates: `{ handlebars }` holding `app.layout(...)` https://docs.djangoproject.com/en/5.1/topics/templates/
	- Realtime: Plotly Dash is for visualizing interactive charts that update in **realtime**, like a monitoring dashboard
		- so we can make sure machines are operating correctly in realtime
		- with plotly dash we can interact with the dashboard's charts for further information why certain metrics are at the state they're in
		- Timeseries data from Machines
			- uptime, downtime is important, data modeled as timeseries data
			- moving averages, windows, rate changes +x% -x%
		- Django (M & V) will serve this data, and Django's Template (T) will act like a shell holding Plotly Dash figures  
- Django ORM (M)
	- Django ORM enables querying/working with Relational databases (SQL) via Object-oriented python code
		- instead of SQL queries
		- Class : Table :: Attribute : Column
		- define class then call class constructor to create objects (like creating rows) `book = Book(name="Neuromancer", year=1984)`
		- both Django ORM and FastAPI Pydantic create data types from classes
		- +PRO: Django includes ORM as apart of the framework
			- with FastAPI you need to include SQLAlchemy, SQLModel for ORM 
	- https://docs.djangoproject.com/en/5.1/topics/db/models/
- Django 
	- Django Controller
	- "to view data visualizations and *interface* with the machine"
	- runserver runs django with default wsgi, but run django with uvicorn for asgi when using async with a lot of data 
		- both django and fastapi support async
	- https://docs.djangoproject.com/en/5.1/topics/http/urls/
### FastAPI
- FastAPI endpoints 
	- backend: endpoints, url routes and restful apis
	- https://github.com/bryanat/MLE-11/blob/main/assignments/week-03-huggingface-fastapi/fast_api_tutorial/app/app.py

## OEE
- OEE: Overall Equipment Effectiveness
- Metrics
	- 85%: "It is often thought that a *World-Class OEE score is **85%***." - https://www.oee.com/world-class-oee/
		- 85% goal - 75% average = 10% diff of cost savings
		- 10% = $xx? : 1% OEE KPI = $xx?
		- "support *world class OEE* initiatives."
		- Robustness
			- 1% downtime = -$xx? : how much money lost?
			- push notifications when down : react-like
				- good benefit of choosing Plotly Dash which is built on top of React
				- React can push notifications to email, another app within mv, 
				- or RN standalone (but CON: not python stack and another app to support)
		- 85% goal similar experience
			- https://github.com/bryanat/Reinforcement-Learning-Unity-3D-Packing/blob/master/docs/images/Slide_02.svg
			- https://github.com/bryanat/Reinforcement-Learning-Unity-3D-Packing/blob/master/docs/images/Slide_03.svg
	- Industry 4.0
		- IoT, CPS, autonomous networks with actuators, "teslafy"
	- Customer data & customer feedback
		- enable machine owners to act and react. "easy to operate and maintain"
		- central hub for internal and external customers to view data visualizations and interface with the machine
		- data visualizations and interface tools for internal and external customers to monitor machines
		- collecting data from our machines in the field and analyzing it to optimize performance, proactively maintain the machines, and provide actionable recommendations to our customers
		- "collecting and analyzing field data to optimize machine performance, proactively maintain equipment, and provide actionable recommendations to customers"
