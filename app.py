import datetime
import streamlit as st
import pandas_datareader as pdr
import cufflinks as cf


import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import datetime




APP_NAME = "Stock App!"

# Page Configuration
st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add some markdown
st.sidebar.markdown("Made with love using [Streamlit](https://streamlit.io/).")
st.sidebar.markdown("# :chart_with_upwards_trend:")

# Add app title
st.sidebar.title(APP_NAME)

# Set start and end point to fetch data
start_date = st.sidebar.date_input('Start date', datetime.datetime(2021, 1, 1))
end_date = st.sidebar.date_input('End date', datetime.datetime.now().date())




df = pd.read_csv('NIFTY 50 _2023.csv')
print(df.head())


# Fetch the data for specified ticker e.g. AAPL from yahoo finance


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)


# Interactive data visualizations using cufflinks
# Create candlestick chart
qf = cf.QuantFig(df, legend='top')


# Technical Analysis Studies can be added on demand
# Add Relative Strength Indicator (RSI) study to QuantFigure.studies
qf.add_rsi(periods=20, color='java')

# Add Bollinger Bands (BOLL) study to QuantFigure.studies
qf.add_bollinger_bands(periods=20,boll_std=2,colors=['magenta','grey'],fill=True)

# Add 'volume' study to QuantFigure.studies
qf.add_volume()

fig = qf.iplot(asFigure=True, dimensions=(800, 600))

# Render plot using plotly_chart
st.plotly_chart(fig)
