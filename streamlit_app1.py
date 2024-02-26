import streamlit as st
from streamlit_gsheets import GSheetsConnection
#import pandas as pd
#import numpy as np

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(
    worksheet="Data",
)
# Print results.
# for row in df.itertuples():
#     st.write(f"{row.name} has a :{row.pet}:")

def calc_effective_fg_pct(fgm, fgm3, fga):
    return (fgm + (0.5*fgm3))/fga

pct = calc_effective_fg_pct(5,3,14)

st.title('Simple Stat Tracker')
number = st.number_input('Insert a number')
st.write('The current number is ', number)
st.write(pct)

st.button("Reset", type="primary")

if st.button('Say hellox'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
