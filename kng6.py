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
        commit_message = (
            "Automated commit for Pair Extraordinaire achievement\n\n"
            "Co-authored-by: ensiferum930 <ensiferum930@gmail.com>\n"
            "Co-authored-by: learnwithums <learnwithums@gmail.com>"
        )
        repo.create_file(
            path="achievement_commit.md",  # File to be created
            message=commit_message,  # Commit message with co-authoring
            content="This is a co-authored commit to achieve the 'Pair Extraordinaire' badge.",  # Content of the file
        )
        print("Co-authored commit created.")
    except Exception as e:
        print(f"Failed to create co-authored commit: {e}")

# Run the function to earn "Pair Extraordinaire"
create_coauthored_commit("learnwithums/test1")
