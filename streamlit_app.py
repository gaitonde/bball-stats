import streamlit as st
import pandas as pd
import numpy as np

def calc_effective_fg_pct(fgm, fgm3, fga):
    return (fgm + (0.5*fgm3))/fga

st.title('Simple Stat Tracker: ' + calc_effective_fg_pct(5,3,14))
