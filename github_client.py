from github import Github
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the GitHub token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise Exception("GitHub token not found. Make sure it's set in the .env file.")

# Initialize the GitHub client
github_client = Github(GITHUB_TOKEN)


# Example: Function to get user info
def get_user_info():
    user = github_client.get_user()
    return {
        "login": user.login,
        "name": user.name,
        "public_repos": user.public_repos,
        "followers": user.followers
    }


# Example: Function to list repositories
def list_repositories():
    user = github_client.get_user()
    repos = user.get_repos()
    repo_list = []
    for repo in repos:
        repo_list.append({
            "name": repo.name,
            "description": repo.description,
            "url": repo.html_url
        })
    return repo_list


# Example: Function to create an issue
def create_issue(repo_name, title, body=""):
    user = github_client.get_user()
    repo = user.get_repo(repo_name)
    issue = repo.create_issue(title=title, body=body)
    return {
        "issue_title": issue.title,
        "issue_url": issue.html_url
    }
