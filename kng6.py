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

        # Get the default branch (typically 'main')
        default_branch = repo.default_branch

        # Check if the file exists on the default branch
        try:
            file = repo.get_contents(file_path, ref=default_branch)
            # If it exists, update the file using its SHA
            repo.update_file(
                path=file_path,
                message=commit_message,
                content=content,
                sha=file.sha,
                branch=default_branch
            )
            print("Co-authored commit updated the existing file.")
        except Exception as e:
            # If the file doesn't exist, create it on the default branch
            if "404" in str(e):
                repo.create_file(
                    path=file_path,
                    message=commit_message,
                    content=content,
                    branch=default_branch
                )
                print("Co-authored commit created a new file.")
            else:
                raise e
    
    except Exception as e:
        print(f"Failed to create co-authored commit: {e}")

# Run the function to earn "Pair Extraordinaire"
create_coauthored_commit("learnwithums/test1")
