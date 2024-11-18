from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def get_demo_page():
    html_content = Path("templates/demo_page.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@app.get("/users", response_class=HTMLResponse)
async def get_users_page():
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    html_content = '<h1 class="text-2xl font-bold my-4">Users</h1> <ul>'
    for user in users:
        html_content += f"<li>{user['name']}</li>"
    html_content += "</ul>"
    return HTMLResponse(content=html_content)
