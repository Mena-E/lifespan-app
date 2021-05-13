import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from joblib import load

# Imports from this application
from app import app

predictor = load('assets/predictor.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Select Happiness Score

            """, className='mb-3'
        ),

        dcc.Markdown(
            """
            Using Lifespan2020 is easy. Just drag the slider to select your happiness score to see a display of your life expectancy in years.

            """, className='mb-5'
        ),

        dcc.Markdown('### Happiness Score (%)'),
        dcc.Slider(id='happiness_score',
                   min=0,
                   max=75,
                   step=5,
                   value=45,
                   marks={n: str(n) for n in range(0, 75, 5)}
                   ),
        dcc.Markdown('', id='output_happy',
                     style={'textAlign': 'left',
                            'font-size': 18},
                     className='mb-5'),

        dcc.Markdown('### Prediction:'),
        dcc.Markdown('', id='prediction-content',
                     style={'textAlign': 'left',
                            'font-size': 18},
                     className='mb-5'),

    ],
    md=6,
)

column2 = dbc.Col(
        [
  
            html.Img(src='assets/mug.jpg', className='img-fluid')
        ]
)

@app.callback(
    Output(component_id='output_happy', component_property='children'),
    [Input(component_id='happiness_score', component_property='value')])
def update_output_div1(input_value):
    return 'You have selected a happiness score of {}%'.format(input_value)


@app.callback(
    Output('prediction-content', 'children'),
    [
        Input('happiness_score', 'value')
    ])

def predict(happiness_score):
  df = pd.DataFrame(columns=['happiness_score'],
                    data=[[happiness_score]])
  y_pred = predictor.predict(df)[0]
  result = round(y_pred, 2)
  return f'You will likely live to {result:.0f} YRS'


layout = dbc.Row([column1, column2])