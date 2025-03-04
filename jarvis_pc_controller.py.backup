import os
import sys
import ctypes
import subprocess

def is_admin():
    """Check if script is running with Admin Privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Restart script with Admin Privileges"""
    if is_admin():
        print("✅ Running with Admin Privileges.")
        return True

    print("⚠️ Requesting Admin Privileges...")

    # Relaunch Script as Admin
    script = os.path.abspath(__file__)
    params = " ".join(f'"{arg}"' for arg in sys.argv[1:])
    command = ["python", script] + sys.argv[1:]

    # Trigger Windows UAC Prompt
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)
    sys.exit(0)  # Exit current process

def main():
    """Main Function to Control PC"""
    if not run_as_admin():
        return

    print("🚀 Jarvis PC Controller is Running...")

if __name__ == "__main__":
    main()
