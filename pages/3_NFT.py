import streamlit as st 
import pandas as pd 
import plotly.express as px
st.set_page_config( 
    page_title="NFT", 
    page_icon="🎴", 
    layout="wide"
)

api_endpoint1 = ('https://node-api.flipsidecrypto.com/api/v2/queries/f2fa8b7a-c020-45ee-b331-ec9a3ac8cec6/data/latest')
df1 = pd.read_json(api_endpoint1) #1-nft mints: https://app.flipsidecrypto.com/velocity/queries/f2fa8b7a-c020-45ee-b331-ec9a3ac8cec6
api_endpoint2 = ('https://node-api.flipsidecrypto.com/api/v2/queries/7c1d518a-12d8-481f-ad6b-506630df74de/data/latest')
df2 = pd.read_json(api_endpoint2) #2-daily nft mints: https://app.flipsidecrypto.com/velocity/queries/7c1d518a-12d8-481f-ad6b-506630df74de
api_endpoint3 = ('https://node-api.flipsidecrypto.com/api/v2/queries/6ac80516-c375-4ea6-b6a0-c52ef2f9d4d8/data/latest')
df3 = pd.read_json(api_endpoint3) #3- Top 10 collections with the most volume of mint: https://app.flipsidecrypto.com/velocity/queries/6ac80516-c375-4ea6-b6a0-c52ef2f9d4d8
api_endpoint00 = ('https://node-api.flipsidecrypto.com/api/v2/queries/a7b209c2-16c9-4621-992a-dd38af31886d/data/latest')
df00 = pd.read_json(api_endpoint00) #00-Category of the number of minters according to volume of NFT mints: https://app.flipsidecrypto.com/velocity/queries/f2fa8b7a-c020-45ee-b331-ec9a3ac8cec6
api_endpoint4 = ('https://node-api.flipsidecrypto.com/api/v2/queries/91d3f240-6860-4487-bffe-066190980afd/data/latest')
df4 = pd.read_json(api_endpoint4) #4-nft sales: https://app.flipsidecrypto.com/velocity/queries/91d3f240-6860-4487-bffe-066190980afd
api_endpoint5 = ('https://node-api.flipsidecrypto.com/api/v2/queries/4152a269-4ac0-4e9a-a610-710492832021/data/latest')
df5 = pd.read_json(api_endpoint5) #5-nft daily sales: https://app.flipsidecrypto.com/velocity/queries/4152a269-4ac0-4e9a-a610-710492832021
api_endpoint6 = ('https://node-api.flipsidecrypto.com/api/v2/queries/580706d8-0976-45e0-99fa-1b8bb0c9e81a/data/latest')
df6 = pd.read_json(api_endpoint6) #6- Top 10 Buyers with the most number of NFT sales: https://app.flipsidecrypto.com/velocity/queries/580706d8-0976-45e0-99fa-1b8bb0c9e81a
api_endpoint7 = ('https://node-api.flipsidecrypto.com/api/v2/queries/cb6df1f9-0302-4e42-9f1f-fdb0cabfb8c8/data/latest')
df7 = pd.read_json(api_endpoint7) #7- Top 10 Buyers with the most volume of NFT sales: https://app.flipsidecrypto.com/velocity/queries/cb6df1f9-0302-4e42-9f1f-fdb0cabfb8c8
api_endpoint8 = ('https://node-api.flipsidecrypto.com/api/v2/queries/ec2de3fb-1563-4632-99c6-6fc5943608ae/data/latest')
df8 = pd.read_json(api_endpoint8) #Category of the number of buyers according to the volume of NFT sales: https://app.flipsidecrypto.com/velocity/queries/ec2de3fb-1563-4632-99c6-6fc5943608ae




st.title('NFT')

st.header('Mints')
st.write("Total number of minted NFTs, minters, and etc. are shown in below single number charts. The number of minters is equal to the wallet addresses on NEAR network which mint NFT." )
c1, c2, c3= st.columns(3)
with c1:
    st.metric(value="{0:,.0f}".format(df1["Total Number of Mints"][0]), label="Total Number of Mints")
    st.metric(value="{0:,.0f}".format(df1["Number of Minted NFTs"][0]), label="Number of Minted NFTs")
with c2:
    st.metric(value="{0:,.0f}".format(df1["Total Number of Minters"][0]), label="Total Number of Minters")
    st.metric(value="{0:,.0f}".format(df1["Total Volume of Mints"][0]), label="Total Volume of Mints")
with c3:
    st.metric(value="{0:,.0f}".format(df1["Total Number of Collections"][0]), label="Total Number of Collections")


fig = px.bar(df2,x='DAY', y='Total Number of Mints', title='Total Number of Daily Mints')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df2,x='DAY', y='Total Number of Minters', title='Total Number of Daily Minters')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df2,x='DAY', y='Number of Minted NFTs', title='Daily Number of Minted NFTs')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df2,x='DAY', y='Total Volume of Mints', title='Total Volume of Mints')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')



c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df3, x='COLLECTION', y='Total Volume of Mints', color='COLLECTION', title='Top 10 collections with the most volume of mint')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    fig = px.pie(df00, values='Number of Minters', names='CAT', title='Category of the number of minters according to volume of NFT mints')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
with c2:
    fig = px.bar(df00, x='CAT', y='Number of Minters', color='CAT', title='Category of the number of minters according to volume of NFT mints')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit') 



st.header('Sales')
st.write("Total number of NFT sales, buyers, and etc. are shown in below single number charts. Daily charts are shown below too." )
c1, c2= st.columns(2)
with c1:
    st.metric(value="{0:,.0f}".format(df4["Total Number of NFT Buyers"][0]), label="Total Number of NFT Buyers")
    st.metric(value="{0:,.0f}".format(df4["Total Number of Sold NFTs"][0]), label="Total Number of Sold NFTs")
with c2:
    st.metric(value="{0:,.0f}".format(df4["Total Number of NFT Sales"][0]), label="Total Number of NFT Sales")
    st.metric(value="{0:,.0f}".format(df4["Total Volume of Sold NFTs"][0]), label="Total Volume of Sold NFTs")


fig = px.bar(df5,x='DAY', y='Total Number of NFT Buyers', title='Total Number of Daily NFT Buyers')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df5,x='DAY', y='Total Number of NFT Sales', title='Total Number of Daily NFT Sales')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df5,x='DAY', y='Total Number of Sold NFTs', title='Total Number of Daily Sold NFTs')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')
fig = px.bar(df5,x='DAY', y='Total Volume of Sold NFTs', title='Total Volume of Sold NFTs')
fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume')
st.plotly_chart(fig, use_container_width=True, theme='streamlit')




c1, c2 = st.columns(2)
with c1:
    fig = px.bar(df6, x='Buyer', y='Total Number of NFT Sales', color='Buyer', title='Top 10 Buyers with the most number of NFT sales')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')
    
    fig = px.bar(df8, x='CAT', y='Number of Buyers', color='CAT', title='Category of the number of buyers according to the volume of NFT sales')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Count', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')

with c2:
    fig = px.bar(df7, x='Buyer', y='Total Volume of Sold NFTs', color='Buyer', title='Top 10 Buyers with the most volume of NFT sales')
    fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title='Volume', xaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig, use_container_width=True, theme='streamlit') 

    fig = px.pie(df8, values='Number of Buyers', names='CAT', title='Category of the number of buyers according to the volume of NFT sales')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme='streamlit')