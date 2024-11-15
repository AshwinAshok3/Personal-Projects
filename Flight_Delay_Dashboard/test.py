# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# importing the libraries
import dash
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import html , dcc
from dash.dependencies import Input , Output

# Importing the dataset
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str,
                                   'Div2Airport': str, 'Div2TailNum': str})


# initializing the application and layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Total flights to the destination state",
    style={'textAlign':'centre',
            'color':'red',
            'font-size':50}),
    html.Br(),
    html.Div(['Year', dcc.Input(id = 'input-year',
                                value='2010',
                                type='number',
                                style={'height':'25px',
                                       'width':'100px',
                                       'color':'blue',
                                       'font-size':20})],
                style={'font-size':20}),
    html.Br(),
    html.Div(dcc.Graph(id='bar-plot')),
    html.Br()
])

# callback decorator
@app.callback(Output(component_id='bar-plot',component_property='figure'),
Input(component_id='input-year',component_property='value'))

# function definition for the decorator
def year_bar_plot(present_year):
    df=airline_data[airline_data['Year']==int(present_year)]

    bar_plot_df = df.groupby('DestState')['Flights'].sum().reset_index()

    bplot_fig = px.bar(bar_plot_df,
                        x=bar_plot_df['DestState'],
                        y=bar_plot_df['Flights'])
    bplot_fig.update_layout(
        title="Total number of Flights to the Destination state split by reporting airline" ,
        xaxis_title = "DestState",
        yaxis_title = "Flights"
    )

    return bplot_fig


if __name__=='__main__':
    app.run_server()