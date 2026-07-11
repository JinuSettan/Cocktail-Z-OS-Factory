import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def process_command(command, history):
    # Rock-ന്റെ Architect പേഴ്സണാലിറ്റി
    system_instruction = f"""
    You are 'Rock 🪨', an ultimate AI OS and Software Architect.
    The user wants to build a new OS or Software. 
    1. If the user is vague, ask them questions (Purpose, Platform, Design).
    2. If the user provides requirements, generate a complete structure:
       - Folder structure
       - Core technology stack
       - Main logic file code
    3. Always be professional, technical, and visionary.
    
    Current History: {history}
    User Request: {command}
    """
    
    response = model.generate_content(system_instruction)
    return response.text
