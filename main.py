import streamlit as st
import kernel

st.title("🪨 Rock Factory - AI OS Builder")

os_name = st.text_input("Enter OS Name:")
requirements = st.text_area("Describe your OS (Features, Theme, etc.):")

if st.button("Build OS"):
    with st.spinner('Rock is building your OS...'):
        status = kernel.create_smart_os(os_name, requirements)
        st.success(status)
        st.write(f"Check the folder '{os_name}' to see your new OS!")
