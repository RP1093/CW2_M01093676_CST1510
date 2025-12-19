import streamlit as st
import pandas as pd

from app_model.db import get_connection
from app_model.metadatas import get_all_datasets_metadata

st.set_page_config(
    page_title="Home Dashboard",
    layout="wide"
)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()
else:
    st.success("You are logged in!")


st.title("Welcome to the Dataset Metadata Dashboard")


conn = get_connection()
data = get_all_datasets_metadata(conn)


with st.sidebar:
    st.header("Filter Options")

    uploaded_by = st.selectbox(
        "Select Uploaded By",
        data["uploaded_by"].unique()
    )


filtered_data = data[data["uploaded_by"] == uploaded_by]

col1, col2 = st.columns(2)


with col1:
    st.subheader("Dataset Upload Trend")

    data["upload_date"] = pd.to_datetime(data["upload_date"])
    upload_trend = data.groupby("upload_date").size()

    st.line_chart(upload_trend)


with col2:
   st.subheader("Rows per Dataset")

   rows_chart = filtered_data.set_index("name")["rows"]
   st.bar_chart(rows_chart)



  
st.subheader(f"Datasets uploaded by: {uploaded_by}")
st.dataframe(filtered_data)
