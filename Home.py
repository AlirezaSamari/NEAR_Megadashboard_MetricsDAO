import streamlit as st 
import pandas as pd 
import plotly.express as px
from PIL import Image

st.set_page_config( 
    page_title="NEAR", 
    page_icon=":wave:", 
    layout="wide"
) 

c1, c2 = st.columns(2)
c1.image(Image.open('Images/near-protocol-near-logo.png'))
with c2:
    st.title('NEAR Protocol')
    st.header('What Is [NEAR Protocol](https://www.kraken.com/learn/what-is-near-protocol)?')
    st.write("NEAR Protocol is a software that aims to incentivize a network of computers to operate a platform for developers to create and launch decentralized applications. Central to NEAR Protocol’s design is the concept of sharding, a process that aims to split the network’s infrastructure into several segments in order for computers, also known as nodes, to only have to handle a fraction of the network’s transactions. ")
'''By distributing segments of the blockchain, rather than the complete blockchain across network participants, sharding is expected to create a more efficient way to retrieve network data and scale the platform.
NEAR operates in a similar manner to other centralized data storage systems like Amazon Web Services (AWS) that serve as the base layer on which applications are built. But rather than being run by a single entity, NEAR is operated and maintained by a distributed network of computers. 
Just as AWS allows developers to deploy code in the cloud without needing to create their own infrastructure, NEAR Protocol facilitates a similar architecture built around a network of computers and its native cryptocurrency, the NEAR token. '''
st.header('Methodology')
st.write('Here we are to have a look at the NEAR network and sometimes we will go deeper into it. First, we check the Overall Activity to have an overview of the network. The number of users and their activities, the amount of fees and gas are examined in this section.')
st.write('Then the swaps are analyzed in terms of number, volume and user. Also, the minting and sale of NFTs have been investigated. The last part deals with Stake review.')
st.write('The [Flipside Crypto](https://flipsidecrypto.xyz/) dataset was used for this analysis, and the queries were written on this website with the SQL Server. This app is made with Python Streamlit framework, which is suitable for data and machine learning related work.The code is placed on GitHub and the link is below.')
st.write('Code Source: (https://github.com/AlirezaSamari/NEAR_Megadashboard_MetricsDAO)')
st.write('Twitter: (https://twitter.com/Elprognerd)')
st.write('Discord Username: Elprognerd#8324')