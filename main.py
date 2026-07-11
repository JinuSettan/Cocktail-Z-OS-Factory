import streamlit as st
import kernel
import interface

# UI Render
interface.render_desktop()

# Session State
if 'history' not in st.session_state:
    st.session_state.history = []

# Chat/Prompt Interface
user_input = st.chat_input("Tell Rock what to build (OS/Software)...")

if user_input:
    # Rock-ന്റെ മാജിക്
    response = kernel.process_command(user_input, st.session_state.history)
    st.session_state.history.append((user_input, response))

# Show Logs
interface.render_terminal(st.session_state.history)
