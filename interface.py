import streamlit as st

def render_desktop():
    st.set_page_config(page_title="Rock OS Factory", layout="wide")
    st.markdown("""
        <style>
        .stApp { background-color: #050505; color: #00ff00; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🪨 Rock Factory - AI OS Architect")
    st.info("System Ready. Define your dream OS below.")

def render_terminal(history):
    st.subheader("Architect Logs")
    for user_msg, rock_res in history:
        with st.chat_message("user"):
            st.write(user_msg)
        with st.chat_message("assistant"):
            st.write(rock_res)
