import streamlit as st
import kernel  # ഇത് നമ്മൾ അടുത്തതായി ഉണ്ടാക്കാൻ പോകുന്ന ഫയലാണ്

st.set_page_config(page_title="Z-OS Factory", layout="wide")

st.title("🚀 Cocktail-Z-OS-Factory")
st.write("Initializing Kernel... System Ready.")

# OS Terminal Interface
if 'history' not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Z-OS Terminal >")

if user_input:
    # kernel.py-ലെ പ്രോസസ്സിംഗ് ഫങ്ഷൻ ഇവിടെ വരും
    response = kernel.process_command(user_input)
    st.session_state.history.append((user_input, response))

for cmd, res in st.session_state.history:
    st.write(f"User: {cmd}")
    st.write(f"Kernel: {res}")

