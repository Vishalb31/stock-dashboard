import pandas as pd
import streamlit as st

url = "https://docs.google.com/spreadsheets/d/1F37oJTWk9kJ7jRk38W2d2bQREKVPalqZIJM7SxT9vXc/export?format=csv"
df = pd.read_csv(url)

st.set_page_config(page_title="📈 Stock Dashboard", layout="wide")
st.title("📈 Live Stock Dashboard")
st.markdown("Powered by Google Sheets + Streamlit")

# Select ticker
tickers = df['Ticker'].unique()
selected_ticker = st.selectbox("Select a Ticker", tickers)

# Filter data for selected ticker
filtered_df = df[df['Ticker'] == selected_ticker]

# Define column names dynamically
close_col = f"Close_{selected_ticker}"
high_col = f"High_{selected_ticker}"
low_col = f"Low_{selected_ticker}"
open_col = f"Open_{selected_ticker}"
volume_col = f"Volume_{selected_ticker}"

# Show KPIs with colored cards using markdown + CSS
latest = filtered_df.iloc[-1]

kpi1 = f"""
<div style="background-color:#4CAF50; padding:10px; border-radius:10px; color:white; width:150px; text-align:center; margin:5px;">
<h4>Close Price</h4>
<h2>₹ {latest[close_col]:.2f}</h2>
</div>
"""

kpi2 = f"""
<div style="background-color:#2196F3; padding:10px; border-radius:10px; color:white; width:150px; text-align:center; margin:5px;">
<h4>Volume</h4>
<h2>{latest[volume_col]:,}</h2>
</div>
"""

kpi3 = f"""
<div style="background-color:#FF5722; padding:10px; border-radius:10px; color:white; width:150px; text-align:center; margin:5px;">
<h4>High</h4>
<h2>₹ {latest[high_col]:.2f}</h2>
</div>
"""

kpi4 = f"""
<div style="background-color:#9C27B0; padding:10px; border-radius:10px; color:white; width:150px; text-align:center; margin:5px;">
<h4>Low</h4>
<h2>₹ {latest[low_col]:.2f}</h2>
</div>
"""

col1, col2, col3, col4 = st.columns(4)
col1.markdown(kpi1, unsafe_allow_html=True)
col2.markdown(kpi2, unsafe_allow_html=True)
col3.markdown(kpi3, unsafe_allow_html=True)
col4.markdown(kpi4, unsafe_allow_html=True)

# Show raw data
st.subheader(f"Raw Data for {selected_ticker}")
st.dataframe(filtered_df)

# Line chart of Close price
st.subheader(f"Closing Price Trend for {selected_ticker}")
filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])
filtered_df = filtered_df.sort_values('Date')
st.line_chart(filtered_df.set_index('Date')[close_col])
