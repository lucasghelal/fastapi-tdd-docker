from fastapi import FastAPI

app = FastAPI(
    version='0.0.2'
)

@app.get("/ping")
def pong():
    return {"ping": "pong!"}