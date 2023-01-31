
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
plt.style.use('fivethirtyeight')


df = pd.read_csv('india_census.csv')

st.title("India Census Analysis")
st.write("Data source:- Kaggle (India Census and Indian Census data with geospatial indexing)")
st.sidebar.title('Analysis')

state_list = df.State.unique().tolist()
# Add Overall India to get analysis of India
state_list.insert(0,'Overall India')
parameter_list = ['Population','Households_with_Internet', 'Housholds_with_Electric_Lighting',	'sex_ratio', 'literacy_rate']

# SideBar
selected_state = st.sidebar.selectbox('Select State ',state_list)
selected_first_param = st.sidebar.selectbox('Select Primary Parameter',parameter_list)
selected_second_param = st.sidebar.selectbox('Select Secondary Parameter',parameter_list)


btn = st.sidebar.button('Click to Plot')

#st.dataframe(df[[selected_first_param, selected_second_param]])


if btn:
    if selected_state == 'Overall India':

        st.info(selected_first_param + " is represented by size")
        st.info(selected_second_param + " is represented by color")

        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude',
                                size=selected_first_param,
                                color=selected_second_param,
                                mapbox_style= "carto-positron", zoom=3, hover_name = 'District',
                                color_continuous_scale=px.colors.sequential.Inferno)

        st.plotly_chart(fig)

        # Sun Burst Chart
        st.info("Sun Burst Chart depicting " + selected_first_param + " distribution for " + selected_state)
        fig = px.sunburst(df, path=['State', 'District'], values=selected_first_param, color= selected_second_param,
                          color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig)

        # Tree Map
        st.info("Tree Map depicting " + selected_first_param + " distribution for " + selected_state)
        fig2 = px.treemap(df, path=[px.Constant('India'), 'State', 'District'], values=selected_first_param,
                          color=selected_second_param, color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig2)

        # Bar Chart
        st.info("Bar Chart depicting " + selected_first_param + " distribution for " + selected_state)
        fig3 = px.bar(df, x='State', y=selected_first_param, color = selected_second_param, text_auto=True,
                      color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig3)

        # Pie Chart
        st.info("Pie Chart depicting " + selected_first_param + " distribution for " + selected_state)
        fig4 = px.pie(df, names='State', values=selected_first_param, color=selected_second_param,
                      color_discrete_sequence=px.colors.sequential.Inferno)
        st.plotly_chart(fig4)

    else:

        st.info(selected_first_param + " is represented by size")
        st.info(selected_second_param + " is represented by color")

        temp_df = df[df.State == selected_state]
        fig = px.scatter_mapbox(temp_df, lat='Latitude', lon='Longitude',
                                size=selected_first_param,
                                color=selected_second_param,
                                mapbox_style="carto-positron", zoom=3, hover_name='District',
                                color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig)

        # Sun Burst Chart
        st.info("Sun Burst Chart depicting " + selected_first_param + " distribution for " + selected_state)
        fig1 = px.sunburst(temp_df, path=['State', 'District'], values=selected_first_param,
                           color= selected_second_param, color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig1)

        # Tree Map
        st.info("Tree Map depicting " + selected_first_param + " distribution for " + selected_state)
        fig2 = px.treemap(temp_df, path=[px.Constant('India'), 'State', 'District'], values=selected_first_param,
                          color= selected_second_param, color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig2)

        # Bar Chart
        st.info("Bar Chart depicting " + selected_first_param + " distribution for " + selected_state)
        fig3 = px.bar(temp_df, x='District', y = selected_first_param, color = selected_second_param, text_auto=True,
                      color_continuous_scale=px.colors.sequential.Inferno)
        st.plotly_chart(fig3)

        # Pie Chart
        st.info("Pie Chart depicting " + selected_first_param + " distribution for " + selected_state)
        fig4 = px.pie(temp_df, names='District', values=selected_first_param, color=selected_second_param,
                      color_discrete_sequence=px.colors.sequential.Inferno)
        st.plotly_chart(fig4)


st.text("END of Analysis")