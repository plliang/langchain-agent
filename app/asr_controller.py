import uvicorn
from fastapi import FastAPI
from asr import FunAsr

app = FastAPI()

app.get("/")
async def index():
    return {"message": "Hello world"}


@app.get("/info")
async def info():
    return {
        "app_name": "FastAPI框架学习",
        "app_version": "v0.0.1"
    }


@app.get("/funasr/")
async def asr(model: str, file: str):
    # model=paraformer-zh
    funasr = FunAsr(model)
    # file=asr_example.wav
    ret = funasr.generate(file)
    return ret


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
