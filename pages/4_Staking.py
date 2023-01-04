import streamlit as st 
import pandas as pd 
import plotly.express as px
st.set_page_config( 
    page_title="NFT", 
    page_icon=":bar_chart:", 
    layout="wide"
)




api1 = 'https://node-api.flipsidecrypto.com/api/v2/queries/2947946f-3125-49fe-b02c-b1cdf88b1e6f/data/latest'
df1 = pd.read_json(api1) #1-overal: https://app.flipsidecrypto.com/velocity/queries/2947946f-3125-49fe-b02c-b1cdf88b1e6f
api2 = 'https://node-api.flipsidecrypto.com/api/v2/queries/80f24d55-463d-4e65-9345-0656d3bb8f4c/data/latest'
df2 = pd.read_json(api2) #2-Total Number of Pools: https://app.flipsidecrypto.com/velocity/queries/80f24d55-463d-4e65-9345-0656d3bb8f4c

st.title('Staking')

st.header('Total Counts & Volumes')
st.write("Total number of users, transactions by the type, total volume and etc. for analyzing staking data are shown in below single number charts. Daily and Percentage charts are shown below too." )
c1, c2, c3, c4= st.columns(4)
with c1:
    st.metric(value="{0:,.0f}".format(df1["Number of Total TXs"][0]), label="Number of Total TXs for Staking")
    st.metric(value="{0:,.0f}".format(df1["Number of Total TXs"][1]), label="Number of Total TXs for Unstaking")
with c2:
    st.metric(value="{0:,.0f}".format(df1["Number of Total Users"][0]), label="Number of Total Users for Staking")
    st.metric(value="{0:,.0f}".format(df1["Number of Total Users"][1]), label="Number of Total Users for Unstaking")
with c3:
    st.metric(value="{0:,.0f}".format(df1["Total Volume"][0]), label="Total Staked Volume")
    st.metric(value="{0:,.0f}".format(df1["Total Volume"][1]), label="Total Unstaked Volume")
with c4:
    st.metric(value="{0:,.0f}".format(df2["Total Number of Pools"][0]), label="Total Number of Pools")

c1, c2, c3 = st.columns(3)
with c1:
    fig = px.pie(df1, values='Number of Total TXs', names='ACTION', title='Percentage of Total TXs (Staking/Unstaking)')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
with c2:
    fig = px.pie(df1, values='Number of Total Users', names='ACTION', title='Percentage of Total Users (Staking/Unstaking)')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
with c3:
    fig = px.pie(df1, values='Total Volume', names='ACTION', title='Percentage of Total Volume (Staking/Unstaking)')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

api3 = 'https://node-api.flipsidecrypto.com/api/v2/queries/d8ec63b8-c2e7-4bdd-a771-3a447044c018/data/latest'
df3 = pd.read_json(api3)# 3-overal daily: https://app.flipsidecrypto.com/velocity/queries/d8ec63b8-c2e7-4bdd-a771-3a447044c018
api3_2 = 'https://node-api.flipsidecrypto.com/api/v2/queries/0b61e465-6d46-4280-ab8b-c1666894719f/data/latest'
df3_2 = pd.read_json(api3_2) # 3_2_Daily net Volume: https://app.flipsidecrypto.com/velocity/queries/0b61e465-6d46-4280-ab8b-c1666894719f

st.header('Daily Charts')
fig = px.line(df3, x='DAY', y='Number of Daily TXs', title='Number of Daily TXs', color='ACTION')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

fig = px.line(df3, x='DAY', y='Number of Daily Users', title='Number of Daily Users', color='ACTION')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

fig = px.bar(df3, x='DAY', y='Total Daily Volume', title='Total Daily Volume', color='ACTION')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

fig = px.line(df3_2, x='DAY', y='Total Daily Net Volume', title='Total Daily Net Volume (= Staking - Unstaking)')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')


api4 = 'https://node-api.flipsidecrypto.com/api/v2/queries/2a7af0c1-cf1d-4f59-9ff5-1498ea8b7a62/data/latest'
df4 = pd.read_json(api4) #4-Top 10 Pools with The Most of The Volume: https://app.flipsidecrypto.com/velocity/queries/2a7af0c1-cf1d-4f59-9ff5-1498ea8b7a62
api5 = 'https://node-api.flipsidecrypto.com/api/v2/queries/b14b7fa8-2577-437e-a185-89d80b43fcac/data/latest'
df5 = pd.read_json(api5) #5-Top 10 Users with The Most Staked Volume at Current Time: https://app.flipsidecrypto.com/velocity/queries/b14b7fa8-2577-437e-a185-89d80b43fcac

st.header('Top 10s')
c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df4, x='Pool Name', y='Current Volume of Pool', title='Top 10 Pools with The Most of The Volume', color='Pool Name')
    fig.update_layout(showlegend=False, xaxis_title='Pool Name', yaxis_title='Volume')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
with c2:
    fig = px.bar(df5, x='User', y='Volume at Current Time', title='Top 10 Users with The Most Staked Volume at Current Time', color='User', height=700)
    fig.update_layout(showlegend=False, xaxis_title='User', yaxis_title='Volume')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')