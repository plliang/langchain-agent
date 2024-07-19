import os.path

import uvicorn
from fastapi import FastAPI,File, UploadFile
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


funasrModel = None


@app.get("/funasr/")
async def asr(model: str, file: str):
    global funasrModel
    if funasrModel is None:
        # model=paraformer-zh
        funasrModel = FunAsr(model)
    # file=asr_example.wav
    ret = funasrModel.generate(file)
    return ret


@app.post("/funasr/upload")
async def upload(file: UploadFile = File(...)):
    filename = file.filename
    save_path = f'./files/'

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    save_file = os.path.join(save_path, filename)

    os_file = open(save_file, 'wb')
    data = await file.read()
    os_file.write(data)
    os_file.close()

    return {'msg': f'{filename}上传成功'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
