from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import requests
from openai import api_key

app = FastAPI()
origins = [
    "http://localhost:4200",  # Angular 開發用的地址
]

# 加入 CORS 中介層
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 或設為 ["*"] 代表允許所有來源（不建議正式環境）
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/kkk/{prompt}")
async def apiapi(prompt: str):
    answer=callModel(prompt)
    return {"apiapi":answer.json()}
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

def callModel(prompt:str):
    api_key = ""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "http://localhost:4200",  # 或你的網站
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o",  # 或用 gpt-4/openai
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": f"{prompt}"},
        ]
    }

    res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
    return res;