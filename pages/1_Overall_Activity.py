import streamlit as st 
import pandas as pd 
import plotly.express as px
st.set_page_config( 
    page_title="User Activity", 
    page_icon="🌍", 
    layout="wide"
) 
 
 


api_endpoint1 = ('https://node-api.flipsidecrypto.com/api/v2/queries/cd0abac9-97f7-4f9c-97f2-1501d0de3479/data/latest')
df1 = pd.read_json(api_endpoint1) #overal: https://app.flipsidecrypto.com/velocity/queries/cd0abac9-97f7-4f9c-97f2-1501d0de3479
api_endpoint2 = ('https://node-api.flipsidecrypto.com/api/v2/queries/21e25665-14f5-4b60-977e-51cf57afcc68/data/latest')
df2 = pd.read_json(api_endpoint2) #daily overal: https://app.flipsidecrypto.com/velocity/queries/21e25665-14f5-4b60-977e-51cf57afcc68

st.title('User Activity')
st.header('Active Users')
st.write("The number of active users is equal to the wallet addresses on NEAR network which are making transactions." )
st.metric(value="{0:,.0f}".format(df1["Number of Active Users"][0]), label="Total Number of Active Users")
fig = px.bar(df2,x='DATE', y='Number of Active Users', title='Number of Daily Active Users')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df2,x='DATE', y='Cumulative Number of Active Users', title='Cumulative Number of Active Users')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.header('Transactions')
st.write("The number of transactions is equal to the total transactions that are made by all users (wallets).")
st.metric(value="{0:,.0f}".format(df1["Number of Txs"][0]), label='Number of Transactions')
fig = px.bar(df2,x='DATE', y='Number of Txs', title='Number of Daily Transactions')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df2,x='DATE', y='Cumulative Number of Txs', title='Cumulative Number of Transactions')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.header('Smart Contracts')
st.write('The number of smart contracts (like trading, investing, lending, and borrowing):' )
st.metric(value="{0:,.0f}".format(df1["Number of Smart Contracts"][0]), label='Number of Smart Contracts')
fig = px.bar(df2,x='DATE', y="Number of Smart Contracts", title='Number of Daily Smart Contracts')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df2,x='DATE', y="Cumulative Number of Smart Contracts", title='Cumulative Number of Smart Contracts')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.header('Near Price')
st.write('The average daily price of NEAR is shown in the chart below.')
fig = px.line(df2,x='DATE', y="Near Price", title='Average Daily Near Price')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Price(USD)')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.header('Transaction Fee')
st.write('The total fees for user transactions are listed below in general and daily.')
st.metric(value="{0:,.0f}".format(df1["Total Tx Fee"][0]), label="Total Transaction Fee (NEAR)")
fig = px.bar(df2,x='DATE', y="Total Tx Fee (NEAR)", title='Total Transaction Fee (NEAR)')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Value (NEAR)')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df2,x='DATE', y="Total Tx Fee in USD", title='Total Transacion Fee in USD')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Value(USD)')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.header('Gas')
st.metric(value="{0:,.0f}".format(df1["GAS_USED"][0]), label="Total Gas Used")
fig = px.bar(df2,x='DATE', y="Total Gas Used", title='Total Gas Used')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Gas')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')



api_endpoint3 = 'https://node-api.flipsidecrypto.com/api/v2/queries/34cc3b64-7592-4ebb-8555-2f466d1af3e1/data/latest'
df3 = pd.read_json(api_endpoint3) #daily new user: https://app.flipsidecrypto.com/velocity/queries/34cc3b64-7592-4ebb-8555-2f466d1af3e1
st.header('New Users')
st.write("The number of users who transact for the first time on the chain is shown in the daily chart below.")
fig = px.line(df3,x='DATE', y='Daily New Users', title='Number of Daily New Users')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')


api_endpoint4 = 'https://node-api.flipsidecrypto.com/api/v2/queries/2af7eaff-61be-4bbd-b349-c1a6151cbff1/data/latest'
df4 = pd.read_json(api_endpoint4) #performance: https://app.flipsidecrypto.com/velocity/queries/2af7eaff-61be-4bbd-b349-c1a6151cbff1
api_endpoint5 = 'https://node-api.flipsidecrypto.com/api/v2/queries/312929fa-e173-4b98-9750-adefb81e7294/data/latest'
df5 = pd.read_json(api_endpoint5) #performance: https://app.flipsidecrypto.com/velocity/queries/312929fa-e173-4b98-9750-adefb81e7294
st.header('Succsessful/Failed Transactions')

c1, c2 = st.columns(2)
with c1:
    st.metric(value="{0:,.0f}".format(df4["Number of Total Txs"][0]), label='Number of Total Transactions')
    st.metric(value="{0:,.0f}".format(df4["Successful Txs Rate"][0]), label='Successful Transactions Rate')
with c2:
    st.metric(value="{0:,.0f}".format(df4["Number of Successful Txs"][0]), label='Number of Successful Transactions')
    st.metric(value="{0:,.0f}".format(df4["Failed Txs Rate"][0]), label='Failed Transactions Rate')

fig = px.line(df5,x='DATE', y='Number of Total Txs', title='Number of Total Daily Transactions')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df5,x='DATE', y='Number of Successful Txs', title='Number of Succsessful Daily Transactions')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df5,x='DATE', y='Successful Txs Rate', title='Successful Daily Transactions Rate')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Ratio')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df5,x='DATE', y='Failed Txs Rate', title='Failed Daily Transactions Rate')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Ratio')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df5,x='DATE', y='Successful Transactions per Hour', title='Successful Transactions per Hour')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df5,x='DATE', y='Successful Transactions per Minute', title='Successful Transactions per Minute')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.line(df5,x='DATE', y='Successful Transaction per Second', title='Successful Transactions per Second')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')