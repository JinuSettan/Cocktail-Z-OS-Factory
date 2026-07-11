import os
import google.generativeai as genai
from pathlib import Path

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

def build_os_files(os_name, requirements):
    base_path = Path(f"Rock_Projects/{os_name}")
    base_path.mkdir(parents=True, exist_ok=True)
    
    # OS components to generate
    files = {
        "main.py": f"print('Welcome to {os_name}')",
        "kernel.py": "def init(): return 'Kernel Loaded'",
        "interface.py": "import streamlit as st\nst.write('UI Ready')",
        "install.sh": "echo 'Installing system dependencies...'"
    }
    
    for filename, default_code in files.items():
        prompt = f"Write professional code for {filename} for an OS named {os_name}. Purpose: {requirements}. Use best coding practices. Return ONLY code."
        response = model.generate_content(prompt)
        
        with open(base_path / filename, "w") as f:
            f.write(response.text.replace("```python", "").replace("```", ""))
            
    return f"✅ {os_name} successfully built!"
