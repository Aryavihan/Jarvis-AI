import schedule
import time
import subprocess

def run_jarvis_tasks():
    print("✅ Jarvis is running its tasks NOW...")  # Debugging Print

    try:
        print("📌 Checking for Jarvis_AI_Updater.py...")
        result1 = subprocess.run(["python", "C:\\Users\\home\\Jarvis-AI\\Jarvis_AI_Updater.py"], capture_output=True, text=True)
        print("📌 Jarvis_AI_Updater.py Output:", result1.stdout)
        if result1.stderr:
            print("❌ Error in Jarvis_AI_Updater.py:", result1.stderr)

        print("📌 Checking for Jarvis_System_Controller.py...")
        result2 = subprocess.run(["python", "C:\\Users\\home\\Jarvis-AI\\Jarvis_System_Controller.py"], capture_output=True, text=True)
        print("📌 Jarvis_System_Controller.py Output:", result2.stdout)
        if result2.stderr:
            print("❌ Error in Jarvis_System_Controller.py:", result2.stderr)

    except Exception as e:
        print(f"❌ Exception Occurred: {e}")

# Debugging: Check if function is being scheduled
print("✅ Scheduling tasks...")

# Immediate Task Trigger (Debugging Mode)
run_jarvis_tasks()

# अब Task को हर 1 मिनट में Trigger करेंगे
schedule.every(1).minutes.do(run_jarvis_tasks)

print("✅ Scheduled Tasks:", schedule.jobs)  # Debugging Output

while True:
    print("✅ Checking if task is executing...")  # Debugging print
    schedule.run_pending()
    time.sleep(10)  # Debugging के लिए 10 सेकंड का Delay
