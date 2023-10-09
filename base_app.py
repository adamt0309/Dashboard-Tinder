# This is the app for the structure of the dashboard itself

#############################################################################################################################
####################################IMPORT DATA AND LIBRARIES################################################################
#############################################################################################################################
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import dash_bootstrap_components as dbc
import os
#from PIL import Image # new import
external_stylesheets = [dbc.themes.MORPH,
                        'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',
                        ]




#tinder_logo = Image.open('./Resources/tinder_logo.png')
#bumble_logo = Image.open('./Resources/bumble.png')
#badoo_logo = Image.open('./Resources/badoo.png')
#heart=Image.open("./Resources/heart.png")
#word_cloud_female = Image.open('./Resources/word_cloud_gender_F.png')
#word_cloud_male = Image.open('./Resources/word_cloud_gender_M.png')

#############################################################################################################################
####################################DATA MANIPULATION PREPPING FOR DASHBOARD#################################################
#############################################################################################################################

df=pd.read_csv("./Data/descriptive_stats.csv")
df_datingapps=pd.read_csv("./Data/datingapps_downloads.csv")
df_datingtrends=pd.read_csv("./Data/datingtrends.csv")

dating_trends_melt=pd.melt(df_datingtrends, id_vars =['Category'], value_vars =['1995', '2017'])
dating_trend_fig = px.bar(dating_trends_melt, x="variable", y="value", color="Category", title="How couples meet").update_layout(
    xaxis_title="Year", yaxis_title="Percentage"
)
dating_trend_fig.layout.yaxis.tickformat = ',.0%'
# dating_trend_fig.add_layout_image(
#     dict(
#         source=heart,
#         xref="paper", yref="paper",
#         x=0.5, y=0.5,
#         sizex=0.3, sizey=0.3
#     )
# )
dating_trend_fig.update_layout(title={'font': {'size': 40}})




downloads_fig = px.bar(df_datingapps, x="Apps ", y="Downloads",title='Dating app downloads globally in 2022', color="Apps ")
downloads_fig.update_yaxes(title_text='Downloads(in millions)')
# downloads_fig.add_layout_image(
#     dict(
#         source=tinder_logo,
#         xref="x", yref="paper",
#         x='Tinder', y=1.1,
#         sizex=1, sizey=1,
#         xanchor="center"
#     )
# )
# downloads_fig.add_layout_image(
#     dict(
#         source=bumble_logo,
#         xref="x", yref="paper",
#         x='Bumble', y=1.1,
#         sizex=1, sizey=1,
#         xanchor="center"
#     )
# )
# downloads_fig.add_layout_image(
#     dict(
#         source=badoo_logo,
#         xref="x", yref="paper",
#         x="Badoo", y=1.1,
#         sizex=1, sizey=1,
#         xanchor="center"
#     )
# )

avg_match_rate_by_gender = df.groupby('gender')['AverageMatchRate'].mean()
avg_match_rate_by_sexuality = df.groupby('sexuality')['AverageMatchRate'].mean()

genders = df["gender"].sort_values().unique()
print(genders)


male_emojis=pd.read_csv("./Data/male_emojis.csv")
female_emojis=pd.read_csv("./Data/female_emojis.csv")
fig_emojis = make_subplots(rows=2, cols=1,subplot_titles=("Male: most used emojis", "Female: most used emojis"))


fig1 = px.bar(male_emojis, x = 'emojis', y = 'volumes')
fig2 = px.bar(female_emojis, x = 'emojis', y = 'volumes')
fig_emojis.add_trace(fig1['data'][0], row=1, col=1)
fig_emojis.add_trace(fig2['data'][0], row=2, col=1)

## App instance
dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#############################################################################################################################
################################################## APP LAYOUT ###############################################################
#############################################################################################################################
header= [
        #html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
                html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.H1(children="Tinder Data Dive", style={"fontSize": "80px", "color": "#ff9999", "text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.Img(src=dash.get_asset_url('TinderPNG.png'),style={'display':'inline-block','height':'20%', 'width':'10%',"text-align":"center"}),
        html.H3(
            children=(
                "A dashboard that analyses the trends, statistics and "
                " generates insight behind the science of dating",
            ), style={"text-align":"center"},
        ),
                html.P("We have sourced data from annonymously aggregated Tinder accounts on likes, match rates, usage and messages. This is a dataset of over a 1,200 users and 200,000 messages!"),
            html.Br(),
            html.Br(),
    ]

column1=[  html.P(children="🥑", className="header-emoji", style={"fontSize": "48px"}),
        html.H1(children="Tinder Data Dive", style={"fontSize": "48px", "color": "red"}),

]

column2=[

]


dash_app.layout = html.Div(    [
        dbc.Row(dbc.Col(header )),
        dbc.Row(
            [
                dbc.Col([
                html.Br(),
                html.H3("Changing habits of dating",style={"text-align":"center"}),
                html.P("Over the past decades, traditional methods of dating has gradually changed to using modern dating apps. Nowadays, this is the standard way in which people meet potential partners."),        
               # Graph showing trend of dating over time - statista
                dcc.Graph(figure=dating_trend_fig),
                html.Br(),
                html.H3("Dating apps",style={"text-align":"center"}),
                html.P("Of all the dating apps, Tinder is by far away the most popular in terms of downloads and usage"),
                dcc.Graph(figure=downloads_fig),
                html.Br(),
                html.H3("Swipes",style={"text-align":"center"}),
                html.P("One of the most interesting piece of statistics is how discerning a tinder user is. Do they rarely swipe right? Or will their hands likely develop RSI from all the repetitive movements? And how different is that for different demographics? "),
                dcc.Dropdown(['gender','sexuality','AgeofUserGroup','educationLevel'],id='swipe-rate-dropdown',value='gender'),
                dcc.Graph(id="swipe-rate-chart"),
                html.Label(), 
                html.Br(),
                html.H3("Matches",style={"text-align":"center"}),
                html.P("Of course, when one looks at Tinder, one of the key things people care about is match rate - how many swipes are needed before there is a match? Is there a difference between male and female?"),
                dcc.Dropdown(['gender','sexuality','AgeofUserGroup','educationLevel'],id='match-rate-dropdown',value='gender'),
                dcc.Graph(id="match-rate-chart"),
      ]),

                ## Second column
                dbc.Col([html.Br(),
                        html.H3("Messages",style={"text-align":"center"}),       
                         html.P("This dataset also includes annonymised messages from every user in this dataset. Some very interesting insights from the messages data can be drawn!"),
                         html.Img(src=dash.get_asset_url('chat_convo.png'),style={'height':'20%', 'width':'85%',"text-align":"center"}),
                            html.P("Note: only messages sent by the user is available, messages sent to the user is not within our dataset."),
                            html.Br(),
                            html.H3("Word clouds",style={"text-align":"center"}), 
                            html.P("Looking at the most common words between males and females, you can see that the most common word used was 'Haha' and 'Lol' respectively. There are some other interesting words - 'gif','width' and 'height' are when gifs are used - it seems that gif usage is higher amongst males than female! Do you spot any other interesting words?"),
                            html.Div([
    dcc.Tabs([
        dcc.Tab(label='Male', children=[
            html.Img(src=dash.get_asset_url('word_cloud_gender_M.png'), style={'height':'85%', 'width':'95%'}),
        ]),
        dcc.Tab(label='Female', children=[
            html.Img(src=dash.get_asset_url('word_cloud_gender_F.png'), style={'height':'95%', 'width':'105%'}),
        ]),
    ])
]),
                 
                            html.Br(),
                            html.H3("Emojis",style={"text-align":"center"}), 
                            html.P("What about emojis usage? What are the most common emojis? Are there any differences between males and females?"),
                            dcc.Graph(figure=fig_emojis),
                            html.Br(),
                            html.H3("Chatbot",style={"text-align":"center"}), 
                            html.P("It is often a hard process to get a match - there are only so many profiles that you will swipe right on, and of the profiles that you like, not everyone will match with you. For those that match, ghosting is a very common occurrence where there is no response after the inital message. Perhaps this is influenced by what the opening message is? "),
                            html.P("A LLM (Large language model) was built and tuned based on the initial opening messages and whether a response was achieved. It aims to predict what are the most successful opening lines in terms of getting a response from your match - try it below for yourself!"),
                            dcc.Textarea(
        placeholder='Enter a value...',
        value='This is a TextArea component',
        style={'width': '100%'}
    ),
            ]),
            ]
        ),
    ### This is a placeholder for links and sources of everythign
    dbc.Row(dbc.Col([
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.H3("Sources and Links"),
        html.P("[1] Changing habits of dating was obtained from https://www.statista.com/"),
        html.P("[2] Information regarding downloads of different dating apps was obtained from https://www.statista.com/"),
        html.P("[3] Changing habits of dating was obtained from https://www.swipestats.io/"),
        html.P("[4] Code used to generate the dashboard can be found in my github, https://github.com/adamt0309/Tinder-Dashboard"),
        
    ] ),
    
    ),   
    ],
)

#############################################################################################################################
################################################### CALLBACKS ###############################################################
#############################################################################################################################

@dash_app.callback(
        
#Defining the output objects, identifying the element and property of the element to be modified
#For example, Output("price-chart", "figure") will update the figure property of the "price-chart" element
    Output("match-rate-chart", "figure"),
    Output("swipe-rate-chart", "figure"),
    

#Input("region-filter", "value") will watch the "region-filter" element and its value property for changes. The argument
#  passed on to the callback function will be the new value of region-filter.value
    Input('match-rate-dropdown', "value"),
    Input('swipe-rate-dropdown', "value"),
    )

# you define the function that’ll be applied when an input changes. It’s worth noticing that the arguments of the function will 
# correspond with the order of the Input objects supplied to the callback. There’s no explicit relationship between the names of the arguments in the function and the values specified in the Input objects.

#Finally, on lines 14 to 54, you define the body of the function. In this case, the function takes the inputs (region, type of avocado,
#  and date range), filters the data, and generates the figure objects for the price and volume charts.

def update_charts(match_value,swipe_value):
    avg_match_rate_by_filter = df.groupby(match_value)['AverageMatchRate'].mean()
    match_rate_fig = px.bar(avg_match_rate_by_filter, x=avg_match_rate_by_filter.index, y=avg_match_rate_by_filter.values, color=avg_match_rate_by_filter.index, title='Match rate percentage by groups')
    match_rate_fig.layout.yaxis.tickformat = ',.0%'
    match_rate_fig.update_yaxes(title_text='Match rate percentage')
    
    avg_swipe_rate_by_filter = df.groupby(swipe_value)['AveragePercentageSwipeRight'].mean()
    swipe_rate_fig = px.bar(avg_swipe_rate_by_filter, x=avg_swipe_rate_by_filter.index, y=avg_swipe_rate_by_filter.values, color=avg_swipe_rate_by_filter.index, title='Rate of swiping "Right"')
    swipe_rate_fig.layout.yaxis.tickformat = ',.0%'
    swipe_rate_fig.update_yaxes(title_text='Swipe right percentage')
    return match_rate_fig, swipe_rate_fig



#############################################################################################################################
################################################### LAUNCH APP###############################################################
#############################################################################################################################

#if __name__ == '__main__':
 #   dash_app.run_server(host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))

app = dash_app.server

 #   tell if this works