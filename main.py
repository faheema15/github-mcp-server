from fastapi import FastAPI, HTTPException
from github_client import get_user_info, list_repositories, create_issue

from pydantic import BaseModel

class IssueRequest(BaseModel):
    repo_name: str
    title: str
    body: str = ""


app = FastAPI(
    title="GitHub MCP Server",
    description="This server exposes GitHub actions through MCP for AI assistants.",
    version="1.0"
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the GitHub MCP Server!"}

# Endpoint to get GitHub user info
@app.get("/github/user")
def github_user_info():
    try:
        user_info = get_user_info()
        return user_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to list repositories
@app.get("/github/repos")
def github_repositories():
    try:
        repos = list_repositories()
        return repos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to create an issue
@app.post("/github/create-issue")
def github_create_issue(request: IssueRequest):
    try:
        result = create_issue(request.repo_name, request.title, request.body)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi.responses import FileResponse

@app.get("/.well-known/ai-plugin.json")
def get_manifest():
    return FileResponse("ai-plugin.json")

@app.get("/openapi.yaml")
def get_openapi_yaml():
    return FileResponse("openapi.yaml")
