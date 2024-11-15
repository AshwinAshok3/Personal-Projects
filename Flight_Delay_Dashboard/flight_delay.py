# A project for flight delayed Statistics

# Flight Delay statistics

# importing the libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input , Output
import plotly.express as px


# importing the datasets
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str,
                                   'Div2Airport': str, 'Div2TailNum': str})


# declaring and initializing the decorator
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1("FLight Delay Time Statistics",
            style={'textAlign':'centre',
                   'font-size':50,
                   'color':'brown'}) ,
    html.Br(),
    html.Div(["Year",
             dcc.Input(
                id='input-year',
                type='number',
                value='2011',
                style={'width':'100px',
                        'height':'40px',
                        'color':'blue',
                        'font-size':'35px',
                        'text-align':'center'}
                        )],
             style={'font-size':45}
             ),
    html.Br(),
    html.Div(dcc.Graph(id='carrier-plot',
                        style={'display':'flex',
                                'width':'70%',}),
             style={'justify-content':'centre'}
            ),
    html.Br(),
    html.Div(dcc.Graph(id='weather-plot',
                        style={'display':'flex',
                                'width':'70%',}),
             style={'justify-content':'centre'}),
    html.Br(),
    html.Div(dcc.Graph(id='nas-plot',
                        style={'display':'flex',
                                'width':'70%',}),
             style={'justify-content':'centre'}),
    html.Br(),
    html.Div(dcc.Graph(id='security-plot',
                        style={'display':'flex',
                                'width':'70%',}),
             style={'justify-content':'centre'}),
    html.Br(),
    html.Div(dcc.Graph(id='late-plot',
                        style={'display':'flex',
                                'width':'70%',}),
             style={'justify-content':'centre'}),
    html.Br()
])


# initializing the decorator
@app.callback([Output(component_id='carrier-plot', component_property='figure'),
              Output(component_id='weather-plot', component_property='figure'),
              Output(component_id='nas-plot', component_property='figure'),
              Output(component_id='security-plot', component_property='figure'),
              Output(component_id='late-plot', component_property='figure')],
              Input(component_id='input-year', component_property='value')
              )

# defining the functions
def displaying_plots(present_year):
    # data selection
    df=airline_data[airline_data['Year'] == int(present_year)]

    # grouping data on the basis of delays occured by Carriers, Weather, NAS, Security, and LateAircrafts
    average_carrier = df.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    average_weather = df.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    average_nas = df.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
    average_security = df.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    average_lates = df.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()

    # plotting the graphs

    # carriers plot
    carrier_plot = px.line(average_carrier,
                           x='Month',
                           y='CarrierDelay',
                           color='Reporting_Airline',
                           title='Average Carrier Delay (Min) by Aircrafts ')

    # Weather Plot
    weather_plot = px.line(average_weather,
                           x='Month',
                           y='WeatherDelay',
                           color='Reporting_Airline',
                           title='Average Weather Delay (Min) by Aircrafts ')

    # NAS Plot
    nas_plot = px.line(average_nas,
                       x='Month',
                       y='NASDelay',
                       color='Reporting_Airline',
                       title='Average NAS Delay (Min) by Aircrafts ')

    # security plot
    security_plot = px.line(average_security,
                            x='Month',
                            y='SecurityDelay',
                            color='Reporting_Airline',
                            title='Average Security Delay (Min) by Aircrafts ')

    # Aircraft late plot
    late_plot = px.line(average_lates,
                        x='Month',
                        y='LateAircraftDelay',
                        color='Reporting_Airline',
                        title='Average Late Aircrafts Delay by Aircrafts ')


    return [carrier_plot, weather_plot, nas_plot, security_plot, late_plot]


# main function running
if __name__ == '__main__':
    app.run_server(debug=False)