import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
