# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

# df = conn.read()
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")

url = "https://docs.google.com/spreadsheets/d/1fQz2Ix6heBb8ORtGFsNqcPodfM79a-29_9WMWHcEJR0/edit"
data = conn.read(spreadsheet=url, usecols=[0, 1])
# Print results.
st.dataframe(data)