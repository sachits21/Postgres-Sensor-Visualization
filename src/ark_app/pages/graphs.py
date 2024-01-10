import psycopg2
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from psycopg2 import pool
import os
import plotly.graph_objects as go
from typing import Optional

dash.register_page(__name__, path='/', name="Ark Biotech Graphs")

#Inputs: Cursor for Postgre database, Table_name for name of sql table in database
#Outputs: Figure of values vs time
def create_plot(cursor: psycopg2.extensions.cursor, table_name: str) -> Optional[go.Figure]:
    try:
        #Query fetches data from table and cursor executes it
        query = f'SELECT * FROM "{table_name}";'
        cursor.execute(query)

        # Fetch all rows from the result of the query
        rows = cursor.fetchall()

        #Get timestamps and values from rows and create and return figure
        if rows:
            timestamps, values = zip(*rows)
            # Create an interactive plot using Plotly
            fig = px.line(x=timestamps, y=values, labels={'x': 'Time', 'y': table_name},
                          title=f'Time vs {table_name} Plot', line_shape='linear')
            
            return fig
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

#Gets Environment Variables and Creates a Connection Pool
dbhost = os.getenv("POSTGRES_HOST")
db = os.getenv("POSTGRES_DB")
user = os.getenv("POSTGRES_USER")
passwd = os.getenv("POSTGRES_PASSWORD")
postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 5, user=user,
                                                    password=passwd,
                                                    host=dbhost,
                                                    port="5432",
                                                    database=db)

conn = postgreSQL_pool.getconn()
cursor = conn.cursor()

#Creates Figures for plots
fig_temp = create_plot(cursor=cursor, table_name='CM_HAM_DO_AI1/Temp_value')
fig_temp.update_layout(yaxis_title="Temperature", title_text="Temperature vs Time", title_x=0.5)

fig_ph = create_plot(cursor=cursor, table_name='CM_HAM_PH_AI1/pH_value')
fig_ph.update_layout(yaxis_title="pH", title_text="pH vs Time", title_x=0.5)

fig_oxygen = create_plot(cursor=cursor, table_name='CM_PID_DO/Process_DO')
fig_oxygen.update_layout(yaxis_title="Distilled Oxygen", title_text="Distilled Oxygen vs Time", title_x=0.5)

fig_pressure = create_plot(cursor=cursor, table_name='CM_PRESSURE/Output')
fig_pressure.update_layout(yaxis_title="Pressure", title_text="Pressure vs Time", title_x=0.5)

postgreSQL_pool.putconn(conn)

#Creates Layout for Graphs
layout = html.Div([
    html.P("You an select specific sections of the plots with cursor, zoom in, or zoom out."),
    html.P("You can also use autoscale to return graph to original state."), 

    html.Div([
        # Temperature vs Time
        dcc.Graph(
            id='Temperature-Plot',
            figure=fig_temp
        ),
        # pH vs Time
        dcc.Graph(
            id='pH-plot',
            figure=fig_ph
        ),
    ], style={'display': 'flex'}), 

    html.Div([
        # Oxygen vs Time
        dcc.Graph(
            id='Oxygen-plot',
            figure=fig_oxygen
        ),
        # Pressure vs Time
        dcc.Graph(
            id='Pressure-plot',
            figure=fig_pressure
        ),
    ], style={'display': 'flex'}),
])