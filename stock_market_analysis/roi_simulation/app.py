# app.py
# streamlit run app.py

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

if not all(Path(p).exists() for p in ("data/final_df.csv", "data/timing_sim.csv", "data/timing_sim_random.csv")):
    import analyze
    analyze.main()   # runs get_data first if the input CSVs are missing

vfinx_df = pd.read_csv("data/vfinx_df.csv", parse_dates=["Date"])
avg_wages = pd.read_csv("data/avg_wages.csv", parse_dates=["Year"])
final_df = pd.read_csv("data/final_df.csv", parse_dates=["Date"])
timing_sim = pd.read_csv("data/timing_sim.csv")
timing_random = pd.read_csv("data/timing_sim_random.csv")

st.set_page_config(page_title="ROI Simulation", layout="wide")
st.subheader("ROI Simulation")

selected_year = st.selectbox("Year", list(range(1980, 2021)), index=40)

df1 = vfinx_df[vfinx_df["Date"].dt.year == selected_year]
df3 = final_df[final_df["Date"].dt.year == selected_year]

fig1 = px.line(df1, x="Date", y="Close", title="VFINX (S&P 500 Index Fund)")
fig2 = px.line(avg_wages, x="Year", y="Avg_Wage", title="Average Wages in United States")
fig3 = px.line(df3, x="Date", y="Investment_Value", color="Frequency", title="Investment Growth")

col1, col2 = st.columns(2)
col1.plotly_chart(fig1)
col2.plotly_chart(fig2)
st.plotly_chart(fig3)

st.divider()
st.subheader("DCA Timing Simulation (1990-2019)")
st.caption("One unit of VFINX bought every month; strategies differ only in the day of the month.")

fig4 = px.bar(timing_sim, x="Strategy", y="Gain_Percent", title="Total Gain % by Purchase Day")
fig5 = px.histogram(timing_random, x="Gain_Percent", nbins=40, title="Random Day: 1000 Iterations")

col3, col4 = st.columns(2)
col3.plotly_chart(fig4)
col4.plotly_chart(fig5)
