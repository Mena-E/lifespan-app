# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How long will you live?

            Your life expectancy may be related to how happy you are.

            Please imagine a ladder, with steps numbered from 0 at the bottom to 10 at the top. 
            The top of the ladder represents the best possible life for you and the bottom of the 
            ladder represents the worst possible life for you. 
            
            On which step of the ladder would 
            you say you personally feel you stand at this time?" This measure is also referred to 
            as Cantril life ladder. Where you stand on the ladder is your happiness score.

            My Life is a running app that can help predict your life expectancy based on your happiness score.

            
            """
        ),
        dcc.Link(dbc.Button('Give My Life a try', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
         html.Img(src='assets/happy_old_woman.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])