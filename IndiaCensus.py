
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india_census.csv')

st.title("India Census")

st.sidebar.title('Analysis')

state_list = df.State.unique().tolist()
# Add Overall India to get analysis of India
state_list.insert(0,'Overall India')
parameter_list = ['Population','Households_with_Internet', 'Housholds_with_Electric_Lighting',	'sex_ratio', 'literacy_rate']

# SideBar
selected_state = st.sidebar.selectbox('Select State ',state_list)
selected_first_param = st.sidebar.selectbox('Select Primary Parameter',parameter_list)
selected_second_param = st.sidebar.selectbox('Select Secondary Parameter',parameter_list)

btn = st.sidebar.button('Plot')

#st.dataframe(df[[selected_first_param, selected_second_param]])

def load_analysis():
    temp_df = df[df.State==selected_state]
    fig = px.scatter_mapbox(temp_df, lat='Latitude', lon = 'Longitude',
                            size=selected_first_param,
                            color=selected_second_param,
                            mapbox_style= "carto-positron", zoom=3, hover_name = 'District')
    st.plotly_chart(fig)

if btn:
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
                                size=selected_first_param,
                                color=selected_second_param,
                                mapbox_style= "carto-positron", zoom=3, hover_name = 'District')
        st.plotly_chart(fig)
    else:
        load_analysis()



