import os
import time

# 🔹 Jarvis AI Self-Coding Engine V1.1 (Bug Fixes)
CODE_FOLDER = "C:\\Users\\home\\Jarvis-AI\\"  # अपने Jarvis के फोल्डर का Path डालें
LOG_FILE = CODE_FOLDER + "jarvis_update_log.txt"

def read_code(file_name):
    """Python Code Read करने का Function"""
    file_path = os.path.join(CODE_FOLDER, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # ✅ UTF-8 Fix
            return file.readlines()
    except FileNotFoundError:
        print(f"⚠️ Warning: {file_name} Not Found!")
        return None

def modify_code(file_name, old_text, new_text):
    """Jarvis पुराने Code को Modify कर सके"""
    file_path = os.path.join(CODE_FOLDER, file_name)
    code = read_code(file_name)

    if code:
        new_code = [line.replace(old_text, new_text) for line in code]
        with open(file_path, "w", encoding="utf-8") as file:  # ✅ UTF-8 Fix
            file.writelines(new_code)
        
        log_update(f"Modified {file_name}: Replaced '{old_text}' with '{new_text}'")
        print(f"✅ {file_name} Successfully Modified!")
    else:
        print(f"⚠️ Skipping Modification: {file_name} Not Found!")

def create_new_agent(agent_name, code_snippet):
    """Jarvis खुद से नया AI Agent बना सके"""
    agent_file = os.path.join(CODE_FOLDER, agent_name + ".py")
    with open(agent_file, "w", encoding="utf-8") as file:  # ✅ UTF-8 Fix
        file.write(code_snippet)
    
    log_update(f"Created New AI Agent: {agent_name}.py")
    print(f"✅ New AI Agent {agent_name}.py Created Successfully!")

def log_update(update_text):
    """Jarvis अपने Updates को Log करेगा"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:  # ✅ UTF-8 Fix
        log.write(f"{time.ctime()} - {update_text}\n")

# 🔹 Example Usage (Jarvis खुद से Code Modify और नया AI Agent Create कर सकता है)
if __name__ == "__main__":
    modify_code("jarvis_trade_logger.py", "Trade Logged", "Jarvis Trade Recorded")
    
    new_agent_code = """# Jarvis AI New Agent
def run():
    print("🚀 AI Agent is Running!")
    
if __name__ == "__main__":
    run()
"""
    create_new_agent("jarvis_ai_agent", new_agent_code)
