from github import Github
import os

# GitHub Personal Access Token (PAT)
GITHUB_TOKEN = os.getenv("KING6")
GITHUB_USERNAME = "ums91"

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)

# Function to co-author a commit for the "Pair Extraordinaire" badge
def create_coauthored_commit(repo_name):
    try:
        repo = g.get_repo(repo_name)
        file_path = "achievement_commit.md"
        commit_message = (
            "Automated commit for Pair Extraordinaire achievement\n\n"
            "Co-authored-by: ums91 <omargoroo91@gmail.com>\n"
            "Co-authored-by: learnwithums <learnwithums@gmail.com>"
        )
        content = "This is a co-authored commit to achieve the 'Pair Extraordinaire' badge."
        
        # Check if the file exists in the repository
        try:
            # If file exists, get its SHA and update it
            file = repo.get_contents(file_path)
            repo.update_file(
                path=file_path,
                message=commit_message,
                content=content,
                sha=file.sha,  # Required SHA for updating
            )
            print("Co-authored commit updated the existing file.")
        except Exception:
            # If the file doesn't exist, create it
            repo.create_file(
                path=file_path,
                message=commit_message,
                content=content,
            )
            print("Co-authored commit created a new file.")
    
    except Exception as e:
        print(f"Failed to create co-authored commit: {e}")

# Run the function to earn "Pair Extraordinaire"
create_coauthored_commit("learnwithums/test1")
