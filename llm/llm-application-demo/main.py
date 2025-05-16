import json
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
import httpx
from pydantic import BaseModel
from pathlib import Path
from sse_starlette.sse import EventSourceResponse

import requests

app = FastAPI()


class TextRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def get_demo_page():
    html_content = Path("templates/demo_page.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html_content)


@app.get("/summarize", response_class=HTMLResponse)
async def get_summarize_page():
    return """
    <h1 class="text-3xl font-bold mb-8">生成式AI用例演示</h1>
    <form hx-post="/summarize" hx-target="#summary-result" class="mb-8">
      <h2 class="text-2xl mb-2">文本摘要</h2>
      <textarea
        name="text"
        rows="4"
        cols="50"
        class="w-full p-2 border border-gray-300 rounded mb-4"
      ></textarea
      ><br />
      <input
        type="submit"
        value="生成摘要"
        class="bg-blue-500 text-white px-4 py-2 rounded"
      />
    </form>
    <div id="summary-result" class="mb-8"></div>
    """


@app.get("/rewrite", response_class=HTMLResponse)
async def get_rewrite_page():
    return """
    <h1 class="text-3xl font-bold mb-8">生成式AI用例演示</h1>
    <form hx-post="/rewrite" hx-target="#rewrite-result" class="mb-8">
      <h2 class="text-2xl mb-2">重写</h2>
      <textarea
        name="text"
        rows="4"
        cols="50"
        class="w-full p-2 border border-gray-300 rounded mb-4"
      ></textarea
      ><br />
      <input
        type="submit"
        value="重写文本"
        class="bg-blue-500 text-white px-4 py-2 rounded"
      />
    </form>
    <div id="rewrite-result" class="mb-8"></div>
    """


@app.get("/extract", response_class=HTMLResponse)
async def get_extract_page():
    return """
    <h1 class="text-3xl font-bold mb-8">生成式AI用例演示</h1>
    <form hx-post="/extract" hx-target="#extract-result" class="mb-8">
      <h2 class="text-2xl mb-2">信息提取</h2>
      <textarea
        name="text"
        rows="4"
        cols="50"
        class="w-full p-2 border border-gray-300 rounded mb-4"
      ></textarea
      ><br />
      <input
        type="submit"
        value="提取信息"
        class="bg-blue-500 text-white px-4 py-2 rounded"
      />
    </form>
    <div id="extract-result" class="mb-8"></div>
    """


@app.get("/qa", response_class=HTMLResponse)
async def get_qa_page():
    return """
    <h1 class="text-3xl font-bold mb-8">生成式AI用例演示</h1>
    <form hx-post="/qa" hx-target="#qa-result" class="mb-8">
      <h2 class="text-2xl mb-2">文本问答</h2>
      <textarea
        name="text"
        rows="4"
        cols="50"
        class="w-full p-2 border border-gray-300 rounded mb-4"
      ></textarea
      ><br />
      <input
        type="submit"
        value="回答问题"
        class="bg-blue-500 text-white px-4 py-2 rounded"
      />
    </form>
    <div id="qa-result" class="mb-8"></div>
    """


@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request):
    form = await request.form()
    text = form["text"]
    # ...existing code...
    return f"<div>{text}</div>"


@app.post("/rewrite", response_class=HTMLResponse)
async def rewrite(request: Request):
    form = await request.form()
    text = form["text"]
    # ...existing code...
    return f"<div>重写后的文本: {text}</div>"


@app.post("/extract", response_class=HTMLResponse)
async def extract(request: Request):
    form = await request.form()
    text = form["text"]
    # ...existing code...
    return f"<div>提取的信息: {text}</div>"


@app.post("/qa", response_class=HTMLResponse)
async def qa(request: Request):
    form = await request.form()
    text = form["text"]
    # ...existing code...
    return f"<div>回答: {text}</div>"

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
async def llm_completion_stream_v1(question: str):

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "user", "content": question}],
        "stream": True
    }

    with requests.post(url, headers=headers, json=payload, stream=True) as r:
        for chunk in r.iter_content(chunk_size=1024, decode_unicode=True):
            yield chunk


@app.post("/v1/llm/completion")
async def llm_completion(request: Request):
    """Test basic completion with OpenRouter's DeepSeek model"""

    question = "write a fancy saas landing page"
    result = llm_completion_stream_v1(question)
    return StreamingResponse(
        result, 
        media_type="text/event-stream", headers={"Cache-Control": "no-cache"}
    )



async def llm_completion_stream_v2(question: str):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [{"role": "user", "content": question}],
        "stream": True
    }
    try:
        async with httpx.AsyncClient() as client:
            async with client.stream('POST', url, headers=headers, json=payload) as response:
                async for line in response.aiter_lines():
                    if not line.strip():
                        # 发送心跳保持连接
                        yield {"event": "ping", "data": ""}
                        continue
                    if line.strip():
                        if line.startswith('data: '):
                            data = line[6:]  # 移除 'data: ' 前缀
                            if data.strip() == '[DONE]':
                                break
                            try:
                                json_data = json.loads(data)
                                content = json_data['choices'][0]['delta'].get('content', '')
                                if content:
                                    yield {"event": "message", "data": content}
                            except json.JSONDecodeError:
                                continue

    except Exception as e:
        yield {"event": "error", "data": str(e)}


@app.post("/v2/llm/completion")
async def llm_completion_v2(request: Request):
    """Test basic completion with OpenRouter's DeepSeek model"""
    question = "write a fancy saas landing page"
    return EventSourceResponse(
        llm_completion_stream_v2(question),
        media_type='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'Connection': 'keep-alive'}
    )