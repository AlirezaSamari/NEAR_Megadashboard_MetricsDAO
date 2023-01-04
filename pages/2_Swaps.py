import streamlit as st 
import pandas as pd 
import plotly.express as px
st.set_page_config( 
    page_title="Swaps", 
    page_icon="🔄", 
    layout="wide"
)

api_endpoint1 = ('https://node-api.flipsidecrypto.com/api/v2/queries/3c81162f-a172-4498-b82d-a3f24dab26f0/data/latest')
df1 = pd.read_json(api_endpoint1) #total swaps, volume: https://app.flipsidecrypto.com/velocity/queries/3c81162f-a172-4498-b82d-a3f24dab26f0
api_endpoint2 = ('https://node-api.flipsidecrypto.com/api/v2/queries/63b9763a-844f-4305-9ece-6498e5449abb/data/latest')
df2 = pd.read_json(api_endpoint2) #daily swaps, volume: https://app.flipsidecrypto.com/velocity/queries/63b9763a-844f-4305-9ece-6498e5449abb

st.title('Swap')

st.header('Swaps and Swappers Count')
st.write("Total number of swaps and swapper are shown in below single number charts. The number of swappers is equal to the wallet addresses on NEAR network which are making swaps (trade assets)." )
c1, c2, c3= st.columns(3)
with c1:
    st.metric(value="{0:,.0f}".format(df1["Total Number of Swaps"][0]), label="Total Number of Swaps")
with c2:
    st.metric(value="{0:,.0f}".format(df1["Total Number of Swappers"][0]), label="Total Number of Swappers")
with c3:
    st.metric(value="{0:,.0f}".format(df1["Total Number of Platforms"][0]), label="Total Number of Platforms")

fig = px.bar(df2,x='day', y='Total Number of Swaps', title='Number of Daily Swaps')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df2,x='day', y='Total Number of Swappers', title='Number of Daily Swappers')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

st.header('Volume of Swaps')
st.write("Total volume of swaps are shown in below single number charts. The total/average daily volume of swap is shown in daily charts below." )
c1, c2, c3= st.columns(3)
with c1:
    st.metric(value="{0:,.0f}".format(df1["Total Volume of Swaps (USD)"][0]), label="Total Volume of Swaps (USD)")
    st.metric(value="{0:,.0f}".format(df1["Average Volume of Swaps (USD)"][0]), label="Average Volume of Swaps (USD)")
with c2:
    st.metric(value="{0:,.0f}".format(df1["Median Volume of Swaps (USD)"][0]), label="Median Volume of Swaps (USD)")
    st.metric(value="{0:,.0f}".format(df1["Maximum Swapped Volume (USD)"][0]), label="Maximum Swapped Volume (USD)")

fig = px.bar(df2,x='day', y='Total Volume of Daily Swap (USD)', title='Total Volume of Daily Swap (USD)')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df2,x='day', y='Average Volume of Daily Swap (USD)', title='Average Volume of Daily Swap (USD)')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

api_endpoint3 = 'https://node-api.flipsidecrypto.com/api/v2/queries/3466ff8a-2d3b-46f1-b592-a3c291dae2b5/data/latest'
df3 = pd.read_json(api_endpoint3) #top 10 swappers with the most of the swap volume: https://app.flipsidecrypto.com/velocity/queries/3466ff8a-2d3b-46f1-b592-a3c291dae2b5
api_endpoint4 = 'https://node-api.flipsidecrypto.com/api/v2/queries/84bce8f7-e384-491b-91eb-2e721e0e8d13/data/latest'
df4 = pd.read_json(api_endpoint4) #top 10 swappers with the most number of the swaps: https://app.flipsidecrypto.com/velocity/queries/84bce8f7-e384-491b-91eb-2e721e0e8d13
api_endpoint5 = 'https://node-api.flipsidecrypto.com/api/v2/queries/d08ffbc6-6337-4ce7-871b-6ee2975cbb01/data/latest'
df5 = pd.read_json(api_endpoint5) #top 10 tokens with the most of the swap volume: https://app.flipsidecrypto.com/velocity/queries/d08ffbc6-6337-4ce7-871b-6ee2975cbb01
api_endpoint6 = 'https://node-api.flipsidecrypto.com/api/v2/queries/99b5b78d-ecf5-4468-805b-86476f921704/data/latest'
df6 = pd.read_json(api_endpoint6) #top 10 tokens with the most number of the swaps: https://app.flipsidecrypto.com/velocity/queries/99b5b78d-ecf5-4468-805b-86476f921704

st.header('Tops')
st.subheader('Top 10 Swappers')
st.write("Top 10 swappers in terms of volume and number of swaps are given in the charts below.")
fig = px.bar(df4, x='Swapper', y='Total Number of Swaps', color='Swapper', title='Top 10 swappers with the most number of the swaps')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
fig.update_xaxes(visible=False)
st.plotly_chart(fig, use_container_width=True, theme='streamlit')

fig = px.bar(df3, x='Swapper', y='Total Volume of Swaps', color='Swapper', title='Top 10 swappers with the most of the swap volume')
fig.update_layout(showlegend=True, xaxis_title=None, yaxis_title='USD', xaxis={'categoryorder':'total descending'})
fig.update_xaxes(visible=False)
st.plotly_chart(fig, use_container_width=True, theme='streamlit')


st.subheader('Top 10 Tokens')
st.write("Top 10 tokens in terms of volume and number of swaps are given in the charts below.")
c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df6, x='TOKEN_IN', y='Total Number of Swaps', color='TOKEN_IN', title='Top 10 tokens with the most number of the swaps')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
with c2:
    fig = px.bar(df5, x='TOKEN_IN', y='Total Volume of Swaps', color='TOKEN_IN', title='Top 10 tokens with the most of the swap volume')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='USD', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')



api_endpoint7 = 'https://node-api.flipsidecrypto.com/api/v2/queries/8ab5bb37-1da7-4e76-b6ff-e6aadca749e2/data/latest'
df7 = pd.read_json(api_endpoint7) #Category of the number of swappers according to the swaps count: https://app.flipsidecrypto.com/velocity/queries/8ab5bb37-1da7-4e76-b6ff-e6aadca749e2
api_endpoint8 = 'https://node-api.flipsidecrypto.com/api/v2/queries/11d7a578-66a0-40c0-9031-cb99a32f489c/data/latest'
df8 = pd.read_json(api_endpoint8) #Category of the number of swappers according to the total swaps volume: https://app.flipsidecrypto.com/velocity/queries/11d7a578-66a0-40c0-9031-cb99a32f489c

st.header('Category of Swappers')
st.write("Grouping number of swappers based on the count and volume of swaps.")
c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df8, x='CAT', y='Number of Swappers', color='CAT', title='Category of the number of swappers according to the total swaps volume')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit') 
    fig = px.bar(df7, x='CAT', y='Number of Swappers', color='CAT', title='Category of the number of swappers according to the swaps count')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')  
    
with c2:
    fig = px.pie(df8, values='Number of Swappers', names='CAT', title=None)
    fig.update_layout(legend_title='Volume of Swaps:', legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    fig = px.pie(df7, values='Number of Swappers', names='CAT', title=None)
    fig.update_layout(legend_title='Count of Swaps:', legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
