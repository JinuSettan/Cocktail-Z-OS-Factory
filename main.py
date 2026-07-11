import streamlit as st
import kernel
import os

st.set_page_config(page_title="Rock OS Factory", layout="wide")

st.title("🪨 Rock Factory - OS Tycoon")

# Project Explorer
if not os.path.exists("Rock_Projects"): os.makedirs("Rock_Projects")
projects = os.listdir("Rock_Projects")

with st.sidebar:
    st.header("Project Explorer")
    selected_os = st.selectbox("Your OS Projects", projects)
    if st.button("Run OS"):
        st.success(f"Launching {selected_os}...")
        # ഇక్కడ OS റൺ ചെയ്യാനുള്ള logic വരും

# OS Building Section
os_name = st.text_input("OS Name:")
reqs = st.text_area("What should Rock build today? (Language, Features, Style):")

if st.button("Build OS Now 🔥"):
    with st.spinner('Rock is building your empire...'):
        msg = kernel.build_os_files(os_name, reqs)
        st.success(msg)

# Sharing Feature
if st.button("Share Project"):
    st.info(f"Link generated for {os_name}: rock-os-factory.com/{os_name}")
