import google.generativeai as genai
import os

# നിന്റെ API കീ ഇവിടെ സെറ്റ് ചെയ്യുക (Secrets-ൽ ആഡ് ചെയ്യുന്നത് മറക്കരുത്)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-1.5-flash')

def process_command(command):
    # OS Kernel-ന്റെ സ്വഭാവം AI-ക്ക് പറഞ്ഞു കൊടുക്കുന്നു
    prompt = f"""
    You are the Kernel of an advanced OS named 'Cocktail-Z-OS'.
    The user is sending commands. You must interpret these commands
    as an OS. If the user asks for files, list them. If they ask to 
    run a program, simulate it. Keep responses brief and technical.
    User command: {command}
    """
    
    response = model.generate_content(prompt)
    return response.text

