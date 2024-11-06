from github import Github
import os

# GitHub Personal Access Token (PAT)
GITHUB_TOKEN = os.getenv("KING6")
GITHUB_USERNAME = "ums91"

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)

# Function to co-author a commit for the "Pair Extraordinaire" badge
def create_coauthored_commit_and_pr(repo_name):
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
        print(f"Using default branch: {default_branch}")

        # Create a new branch for the commit
        new_branch = f"{default_branch}_pair_extraordinaire"
        base = repo.get_branch(default_branch)
        repo.create_git_ref(ref=f'refs/heads/{new_branch}', sha=base.commit.sha)
        print(f"Created a new branch: {new_branch}")

        # Check if the file exists on the default branch
        try:
            # Try to get the file content from the default branch
            file = repo.get_contents(file_path, ref=default_branch)
            print(f"File exists with SHA: {file.sha}")

            # If the file exists, update it using its SHA
            repo.update_file(
                path=file_path,
                message=commit_message,
                content=content,
                sha=file.sha,  # Use the file's SHA for updates
                branch=new_branch
            )
            print("Co-authored commit updated the existing file.")
        except Exception as e:
            if "404" in str(e):
                print("File does not exist. Creating a new file.")
                # If the file doesn't exist, create it on the new branch
                repo.create_file(
                    path=file_path,
                    message=commit_message,
                    content=content,
                    branch=new_branch
                )
                print("Co-authored commit created a new file.")
            else:
                print(f"Error checking file existence: {e}")
                raise e

        # Create a pull request
        pr_title = "Add co-authored commit for Pair Extraordinaire"
        pr_body = "This PR contains a co-authored commit to trigger the 'Pair Extraordinaire' achievement."
        pr = repo.create_pull(
            title=pr_title,
            body=pr_body,
            head=new_branch,
            base=default_branch
        )
        print(f"Pull request created: {pr.title}")

    except Exception as e:
        print(f"Failed to create co-authored commit and PR: {e}")

# Run the function to earn "Pair Extraordinaire"
create_coauthored_commit_and_pr("ums91/KING6")
