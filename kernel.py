import google.generativeai as genai
import os

# API Configuration
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

# Blue Whale Configuration: Flash-1.5 is perfect for fast, logical OS tasks
model = genai.GenerativeModel('gemini-1.5-flash')

# Simulated Persistent Storage & Memory
system_state = {
    "files": ["system.sys", "boot.bin", "user.dat"],
    "running_processes": [],
    "memory_usage": "12%"
}

def process_command(command):
    # Blue Whale System Instruction: Technical, Fast, OS-level Logic
    system_instruction = f"""
    You are the core Kernel of 'Cocktail-Z-OS'. 
    Current System Status: {system_state}
    
    Rules:
    1. If command is 'ls', list current files.
    2. If command is 'run <app>', add to running_processes.
    3. If command is 'mem', show memory usage.
    4. Maintain technical integrity.
    
    User Command: {command}
    """
    
    try:
        response = model.generate_content(system_instruction)
        # ഇവിടെ നമുക്ക് മറുപടിയെ കൂടുതൽ സ്മാർട്ട് ആക്കാം
        return response.text
    except Exception as e:
        return f"KERNEL ERROR: {str(e)}"
