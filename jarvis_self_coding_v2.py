import os
import ast
import time

# 🔹 Jarvis AI Self-Coding Engine V2 (With Debugging & Optimization)
CODE_FOLDER = "C:\\Users\\home\\Jarvis-AI\\"  # अपने Jarvis के फोल्डर का Path डालें
LOG_FILE = CODE_FOLDER + "jarvis_update_log.txt"

def read_code(file_name):
    """Python Code Read करने का Function"""
    file_path = os.path.join(CODE_FOLDER, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"⚠️ Warning: {file_name} Not Found!")
        return None

def debug_code(file_name):
    """Jarvis Python Code को Debug करेगा और Errors Detect करेगा"""
    file_path = os.path.join(CODE_FOLDER, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code_content = file.read()
        
        ast.parse(code_content)  # AST (Abstract Syntax Tree) से Code को Parse करके Check करेंगे
        print(f"✅ No Errors Found in {file_name}!")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax Error in {file_name}: {e}")
        return False

def optimize_code(file_name):
    """Jarvis Code को Optimize करेगा (Unnecessary Code Remove करेगा)"""
    file_path = os.path.join(CODE_FOLDER, file_name)
    code = read_code(file_name)
    
    if code:
        optimized_code = []
        for line in code:
            if not line.strip().startswith("#"):  # 🔹 Comments Remove करेंगे
                optimized_code.append(line)
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(optimized_code)

        log_update(f"Optimized {file_name}: Removed Comments & Extra Spaces")
        print(f"✅ {file_name} Successfully Optimized!")

def log_update(update_text):
    """Jarvis अपने Updates को Log करेगा"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"{time.ctime()} - {update_text}\n")

# 🔹 Example Usage (Jarvis खुद से Code Debug और Optimize करेगा)
if __name__ == "__main__":
    target_file = "jarvis_ai_agent.py"  # जिस File को Debug और Optimize करना है

    if debug_code(target_file):
        optimize_code(target_file)
