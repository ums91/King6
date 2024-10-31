from github import Github
import requests
import time
import os

# GitHub Personal Access Token (PAT)
GITHUB_TOKEN = os.getenv("KING6")
GITHUB_USERNAME = "ums91"

# Authenticate with GitHub
g = Github(GITHUB_TOKEN)

# Function to automate Pull Request creation for "Pull Shark" achievement
def create_pull_request(repo_name):
    try:
        repo = g.get_repo(repo_name)
        pr = repo.create_pull(
            title="Automated PR for GitHub Badge",
            body="Automated pull request to earn GitHub achievements",
            head="main",  # Customize if the default branch is different
            base="main",
        )
        print(f"Pull Request created in {repo_name}: {pr.html_url}")
    except Exception as e:
        print(f"Failed to create pull request in {repo_name}: {e}")

# Function to co-author a commit for "Pair Extraordinaire" badge
def create_coauthored_commit(repo_name):
    repo = g.get_repo(repo_name)
    try:
        repo.create_file(
            "/achievement_commit.md",
            "Automated commit for Pair Extraordinaire achievement",
            "This is a co-authored commit to achieve the 'Pair Extraordinaire' badge.",
            committer={"name": "ums91", "email": "omargoroo91@gmail.com"},
            author={"name": "learnwithums", "email": "learnwithums@gmail.com"},  # Replace with a collaborator’s email
        )
        print("Co-authored commit created.")
    except Exception as e:
        print(f"Failed to create co-authored commit: {e}")

# Function to sponsor a contributor for "Public Sponsor" badge (manual action required)
def public_sponsor():
    print("To earn the 'Public Sponsor' badge, go to GitHub Sponsors and support an open-source contributor.")

# Function to merge a pull request for "YOLO" badge
def merge_pr_without_review(repo_name):
    repo = g.get_repo(repo_name)
    try:
        # Retrieve all open PRs in the repository
        prs = repo.get_pulls(state='open')
        if prs.totalCount > 0:
            pr = prs[0]
            pr.merge(merge_method='merge')
            print(f"Pull request merged without review in {repo_name}.")
        else:
            print("No open pull requests found to merge without review.")
    except Exception as e:
        print(f"Failed to merge pull request without review in {repo_name}: {e}")

# Automate actions to earn badges
def earn_badges():
    # Pull Shark: Create PRs in popular repositories
    create_pull_request("learnwithums/test1")  # Replace with repositories that have stars

    # Pair Extraordinaire: Create co-authored commit
    create_coauthored_commit("learnwithums/test1")  # Replace with your repository

    # Public Sponsor: Requires manual action
    public_sponsor()

    # YOLO: Merge PR without review
    merge_pr_without_review("learnwithums/test1")  # Replace with your repository

# Run the badge-earning actions
earn_badges()
