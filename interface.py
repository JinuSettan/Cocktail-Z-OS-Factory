
import streamlit as st

def render_desktop():
    # OS Header
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; color: white; }
        .terminal { font-family: 'Courier New', monospace; background: black; padding: 20px; border-radius: 10px; }
        </style>
    """, unsafe_allow_html=True)
    
    st.header("💻 Cocktail-Z-OS Desktop")
    
    # Status Bar
    col1, col2, col3 = st.columns(3)
    col1.metric("CPU Load", "4%")
    col2.metric("RAM", "128MB")
    col3.metric("Status", "Online")
    
    st.divider()

def render_terminal(history):
    st.subheader("Terminal Access")
    terminal_container = st.container(height=300)
    with terminal_container:
        for cmd, res in history:
            st.write(f"**> {cmd}**")
            st.write(res)
