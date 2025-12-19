import streamlit as st
from hashing import generate_hash, is_valid_hash
from app_model.db import get_connection
from app_model.users import add_user, get_user

conn = get_connection()

st.set_page_config(
    page_title="Home Dashboard",
    layout="wide"
)

st.title('Welcome to the Main Page')


if st.button("Log In", key="main_login_button"):
    st.session_state['logged_in'] = True

tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", key="login_password")

    
    if st.button("Log In", key="tab_login_button"):
        user = get_user(conn, login_username)

        if user is not None:
            id, user_name, user_hash = user

            if login_username == user_name and is_valid_hash(login_password, user_hash):
                st.session_state['logged_in'] = True
                st.success("Logged in Successfully!")
                st.switch_page("pages/1_dashboard.py")
            else:
                st.session_state['logged_in'] = False
                st.error("Invalid username or password")
        else:
            st.error("User not found")







    








