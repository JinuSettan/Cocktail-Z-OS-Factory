import streamlit as st
import kernel
import os

st.set_page_config(page_title="Cocktail-Z-OS Factory", layout="wide")

# Custom Styling for "Rock" Feel
st.markdown("""<style>
    .stApp { background-color: #0e1117; color: #00ffcc; }
    .stButton>button { border: 2px solid #00ffcc; background: transparent; color: #00ffcc; }
</style>""", unsafe_allow_html=True)

st.title("🪨 Cocktail-Z-OS Factory: Ultimate AI Architect")

# Sidebar - Project Explorer & Features
with st.sidebar:
    st.header("🚀 OS Features Dashboard")
    features = [
        "1. Auto-Kernel Build", "2. Encrypted File System", "3. Cloud Sync", 
        "4. Live Debugging", "5. Plugin Support", "6. Custom GUI Engine",
        "7. AI Terminal Integration", "8. Version Control", "9. One-Click Install",
        "10. Cross-Platform API", "..." # 50 വരെ നീ ഇതിൽ ആഡ് ചെയ്താൽ മതി
    ]
    st.multiselect("Enable Features for New Build:", features)
    
    st.header("Project Explorer")
    if not os.path.exists("Rock_Projects"): os.makedirs("Rock_Projects")
    projects = os.listdir("Rock_Projects")
    selected_os = st.selectbox("Your Projects", projects)
    if st.button("Run/Deploy OS"):
        st.info(f"Deployment initiated for {selected_os}...")

# Main Builder
os_name = st.text_input("Enter OS Name:")
reqs = st.text_area("System Architecture & Features Requirements:")

if st.button("Build OS Empire 🥵🔥"):
    if os_name:
        with st.spinner('Rock is engineering your OS architecture...'):
            msg = kernel.build_os_files(os_name, reqs)
            st.success(msg)
            st.balloons()
    else:
        st.error("OS Name is required to start the factory!")
