from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from pathlib import Path

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def get_demo_page():
    html_content = Path("templates/demo_page.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)
