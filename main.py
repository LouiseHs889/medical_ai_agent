from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
    return {"apiapi": f"Hello {prompt}"}
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
