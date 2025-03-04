import requests
import base64

def git_commit_push(token, repo_name, file_path, commit_message):
    # GitHub API URL
    url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"

    # फाइल को पढ़ें
    with open(file_path, 'r') as file:
        content = file.read()

    # API Token को headers में डालें
    headers = {'Authorization': f'token {token}'}  # यहाँ API Token डालें

    # फाइल को base64 में एन्कोड करें
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    # डाटा तैयार करें
    data = {
        "message": commit_message,
        "content": encoded_content,  # base64 एन्कोडिंग
    }

    # API कॉल करें
    response = requests.put(url, headers=headers, json=data)
    
    # Response चेक करें
    if response.status_code == 201:
        print(f"File {file_path} committed successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# यहाँ अपना GitHub API Token डालें
token = "admin:enterprise, admin:gpg_key, admin:org, admin:org_hook, admin:public_key, admin:repo_hook, admin:ssh_signing_key, audit_log, codespace, copilot, delete:packages, delete_repo, gist, notifications, project, repo, user, workflow, write:discussion, write:network_configurations, write:packages"  # <-- यहाँ API Token डालें

# यहाँ अपनी GitHub रिपॉजिटरी का नाम डालें (उदाहरण: username/repository_name)
repo_name = "username/repo_name"

# यहाँ जिस फाइल को आप GitHub पर पुश करना चाहते हैं, उसका पथ डालें
file_path = "path/to/your/file.txt"

# Commit message डालें
commit_message = "Added a new file"

# अब commit और push करने के लिए फंक्शन कॉल करें
git_commit_push(token, repo_name, file_path, commit_message)
