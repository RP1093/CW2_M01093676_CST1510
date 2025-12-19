import streamlit as st
import pandas as pd

from app_model.db import get_connection
from app_model.cyber_incidents import get_all_cyber_incidents

st.set_page_config(
    page_title="Cyber Incidents Dashboard",
    layout="wide"
)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()
else:
    st.success("You are logged in!")


st.title("Welcome to the Cyber Incidents Dashboard")


conn = get_connection()
data = get_all_cyber_incidents(conn)


with st.sidebar:
    st.header("Filter Options")

    category = st.selectbox(
        "Select Category",
        data["category"].unique()
    )


filtered_data = data[data["category"] == category]

col1, col2 = st.columns(2)


with col1:
    st.subheader("Incident Trend Over Time")

    data["timestamp"] = pd.to_datetime(data["timestamp"])
    incident_trend = data.groupby(data["timestamp"].dt.date).size()

    st.line_chart(incident_trend)


with col2:
    st.subheader("Severity per Incident")

    severity_chart = filtered_data["severity"].value_counts()
    st.bar_chart(severity_chart)


st.subheader(f"Incidents in Category: {category}")
st.dataframe(filtered_data)



  
