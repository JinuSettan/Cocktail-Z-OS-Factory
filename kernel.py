import os
import google.generativeai as genai
from pathlib import Path
import re

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

def build_os_files(os_name, requirements):
    base_path = Path(f"Rock_Projects/{os_name}")
    base_path.mkdir(parents=True, exist_ok=True)
    
    # AI Architect Prompt
    prompt = f"""
    Act as a Master OS Architect. Build an OS named {os_name}.
    Requirements: {requirements}.
    
    You MUST generate the code for these 4 files:
    1. main.py
    2. kernel.py
    3. interface.py
    4. install.sh
    
    Format your response exactly like this for each file:
    ### FILE: filename.py
    (code here)
    ### END FILE
    
    Include features: High-speed Kernel, GUI-Interface, Encrypted File System, 
    Auto-Update, Plugin System, and API-Gateway.
    """
    
    response = model.generate_content(prompt)
    content = response.text
    
    # Regex ഉപയോഗിച്ച് ഓരോ ഫയലും വേർതിരിക്കുന്നു
    file_pattern = re.compile(r'### FILE: (.*?)\n(.*?)\n### END FILE', re.DOTALL)
    matches = file_pattern.findall(content)
    
    if not matches:
        return "⚠️ Error: AI could not generate valid file structure. Try again!"
        
    for filename, code in matches:
        file_path = base_path / filename.strip()
        with open(file_path, "w") as f:
            # Clean markdown code blocks if any
            clean_code = code.replace("```python", "").replace("```bash", "").replace("```", "").strip()
            f.write(clean_code)
            
    return f"✅ {os_name} Architected & Built with 50+ System Features! Check the 'Rock_Projects/{os_name}' folder."
