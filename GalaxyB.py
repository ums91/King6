import requests
import time

# Set your GitHub credentials and target repository details
GITHUB_TOKEN = os.getenv("KING6")  # Replace with your GitHub token
USERNAME = 'ums91'  # Your GitHub username
REPO_OWNER = 'learnwithums'  # Replace with the owner of the target public repo
REPO_NAME = 'test1'  # Replace with the target public repo name

# Headers for authentication
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Step 1: Create a new issue
def create_issue():
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'
    data = {
        'title': 'Achieving Galaxy Brain Badge: Discussion Thread',
        'body': 'This is an open discussion for ideas and feedback!'
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 201:
        issue_number = response.json()['number']
        print(f"Issue created successfully! Issue Number: {issue_number}")
        return issue_number
    else:
        print("Failed to create issue:", response.json())
        return None

# Step 2: Add comments to the issue
def add_comments(issue_number):
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments'
    for i in range(50):  # Adjust the range for the desired number of comments
        data = {
            'body': f'This is comment number {i + 1} to help achieve the Galaxy Brain badge!'
        }
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            print(f"Comment {i + 1} added successfully!")
        else:
            print("Failed to add comment:", response.json())
            break
        
        # Delay to avoid rate limits
        time.sleep(1)

# Execute the script
issue_number = create_issue()
if issue_number:
    add_comments(issue_number)
