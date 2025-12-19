import streamlit as st

from app_model.db import get_connection
from app_model.it_tickets import get_all_tickets


st.set_page_config(
    page_title="IT Operations Dashboard",
    layout="wide"
)


if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()


st.title("IT Operations Dashboard")
 
conn = get_connection()
data = get_all_tickets(conn)


with st.sidebar:
    status = st.selectbox(
        "Filter by Status",
        data["status"].unique()
    )

filtered_data = data[data["status"] == status]


col1, col2 = st.columns(2)

with col1:
    st.subheader("Tickets by Status")
    status_counts = data["status"].value_counts()
    st.bar_chart(status_counts)

with col2:
    st.subheader("Tickets per Staff")
    staff_counts = data["assigned_to"].value_counts()
    st.bar_chart(staff_counts)


st.subheader(f"Tickets with status: {status}")
st.dataframe(filtered_data)
