from fastapi import FastAPI, Request
from service.api.api import main_router
import onnxruntime as rt
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


app = FastAPI(project_name='Emotion_detection')
app.include_router(main_router)

providers = ['CPUExecutionProvider']
model = rt.InferenceSession('service/core/logic/vit_quantized.onnx', providers=providers)


# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.get('/', response_class=FileResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "Rahul"})

# its service.main: app