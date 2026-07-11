import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def create_smart_os(os_name, requirements):
    os.makedirs(os_name, exist_ok=True)
    
    # ഫയലുകളുടെ പട്ടിക
    files = ["interface.py", "kernel.py", "main.py", "requirements.txt"]
    
    for filename in files:
        # Gemini-യോട് പറയുന്നു: ഈ ഫയലിന് വേണ്ട കോഡ് എഴുതിത്തരാൻ
        prompt = f"Write the python code for {filename} for an OS named {os_name} that has these requirements: {requirements}. Return ONLY the code."
        response = model.generate_content(prompt)
        
        # ജനറേറ്റ് ചെയ്ത കോഡ് ഫയലിലേക്ക് സേവ് ചെയ്യുന്നു
        with open(f"{os_name}/{filename}", "w") as f:
            f.write(response.text.replace("```python", "").replace("```", ""))
            
    return f"🚀 {os_name} successfully built by Rock Factory using Gemini AI!"
