# GitHub MCP Server Integration

This project demonstrates a **Model Context Protocol (MCP) Server** that integrates with the **GitHub API**. It allows AI Assistants like Claude or OpenAI GPT to interact with GitHub using MCP.

---

## 🌐 Live Demo

👉 [Deployed Server Link](https://github-mcp-server-production.up.railway.app)  
👉 `.well-known/ai-plugin.json` endpoint:  
```
https://github-mcp-server-production.up.railway.app/.well-known/ai-plugin.json
```

---

## 📖 Project Overview

This MCP Server exposes a REST API that allows AI Assistants to:
- Get user GitHub profile information
- List repositories for a user
- Create an issue in a repository

The server follows **Model Context Protocol (MCP)** standards to ensure interoperability with AI systems.

---

## 🔧 Tech Stack
- **FastAPI** (Python framework for building APIs)
- **OpenAPI** (Standard for describing REST APIs)
- **ai-plugin.json** (MCP metadata configuration)
- **GitHub REST API v3**
- **Deployed on Railway**

---

## ✨ Features
- MCP-compliant server with OpenAPI documentation
- Secure interaction with GitHub using a personal access token
- AI Assistants can:
  - Fetch GitHub user details
  - List repositories by username
  - Create issues on repositories

---

## 📂 Project Structure

```
├── ai-plugin.json             # MCP Plugin metadata for AI Assistants
├── openapi.yaml               # OpenAPI spec describing the available endpoints
├── main.py                    # FastAPI MCP server code
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (this file)
```

---

## 🚀 How It Works

### 1. FastAPI Server
- Exposes REST API endpoints like:
  - `/github/user`
  - `/github/repos/{username}`
  - `/github/repos/{owner}/{repo}/issues`

### 2. ai-plugin.json
- Metadata for AI assistants to understand the MCP server:
  - Plugin name, description
  - Authentication method
  - OpenAPI URL reference

### 3. openapi.yaml
- Defines all routes and parameters for the AI assistant to interact with.

---

## 🔐 Authentication

- **GitHub Personal Access Token (PAT)**
  - Set as an environment variable: `GITHUB_TOKEN`
  - Use in your `.env` file or directly in Railway's environment settings.

---

## ⚙️ Setup Instructions (Local Development)

### Prerequisites:
- Python 3.9+
- GitHub Personal Access Token (PAT) with `repo` permissions

### Clone the repo:
```bash
git clone https://github.com/yourusername/github-mcp-server.git
cd github-mcp-server
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Create `.env` file:
```bash
GITHUB_TOKEN=your_personal_access_token
```

### Run the FastAPI server:
```bash
uvicorn main:app --reload
```

Visit: `http://localhost:8000/docs` for the Swagger UI

---

## 🌍 Deployment (Railway)

1. Login at [Railway](https://railway.app)
2. Create a new project → Deploy from GitHub → Select your MCP repo
3. Add the `GITHUB_TOKEN` as an environment variable in Railway
4. Confirm the start command:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
5. Deploy & get your production URL (e.g., `https://github-mcp-server-production.up.railway.app`)

---

## 🤖 Demonstration with AI Assistants

### Claude AI / OpenAI GPT Plugin (optional based on access)
- Register your `.well-known/ai-plugin.json` URL in the AI assistant settings.
- Interact using natural language prompts:
  ```
  "List my GitHub repositories."
  "Create an issue in my repo named 'sample-repo'."
  ```

---

## 📜 OpenAPI Endpoints

| Endpoint                           | Method | Description                   |
|------------------------------------|--------|-------------------------------|
| `/github/user`                     | GET    | Get authenticated user info   |
| `/github/repos/{username}`         | GET    | List repositories of a user   |
| `/github/repos/{owner}/{repo}/issues` | POST   | Create an issue in a repo     |

---

## 📝 Example Requests

#### Get user info
```bash
curl -X GET https://github-mcp-server-production.up.railway.app/github/user
```

#### List repos
```bash
curl -X GET https://github-mcp-server-production.up.railway.app/github/repos/<username>
```

#### Create an issue
```bash
curl -X POST https://github-mcp-server-production.up.railway.app/github/repos/<owner>/<repo>/issues \
  -H "Content-Type: application/json" \
  -d '{"title": "Bug found!", "body": "Please fix this bug."}'
```

---
