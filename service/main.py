from fastapi import FastAPI
from service.api.api import main_router
import onnxruntime as rt

app = FastAPI(project_name='Emotion_detection')
app.include_router(main_router)

providers = ['CPUExecutionProvider']
model = rt.InferenceSession('service/core/logic/vit_quantized.onnx', providers=providers)

@app.get('/')
async def root():
    return {'hello': 'world'}

# its service.main: app