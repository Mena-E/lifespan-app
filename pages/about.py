# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## About Mena
            I am a Data Scientist with a passion for sports analytics. I harbor some interest in applying Data Science and Statistical analysis to gain a better understanding of social and economic issues. But my deepest fascination lies in how to apply Data Science to help the world transition from our centuries old reliance on fossil fuels to cleaner more sustainable energy sources.
            """, className='mb-5'),
        
        #dcc.Markdown('## About Mena ', className='mb-10'),
        dcc.Markdown('', className='mb-5'),
        html.P(
                [

                    html.Img(src='assets/mena.png', className='img-fluid', height=600, width=600) 

                ], 
                className='mb-5')
    ],md=6
    )

column2 = dbc.Col(
    [
         #html.Img(src='assets/happy_old_woman.jpg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])
