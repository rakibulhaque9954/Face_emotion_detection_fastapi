from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
import numpy as np
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from service.core.logic.onnx_inference import emotions_detector
from service.core.schemas.output import APIOutput
from fastapi import Request
from service.core.logic.system_monitor import monitor_memory_usage
import psutil

detect_router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Get CPU usage as a percentage
cpu_usage = psutil.cpu_percent(interval=1)  # Check every 1 second
print(f"CPU Usage 1: {cpu_usage}%")
monitor_memory_usage()

@detect_router.post('/detect', response_class=HTMLResponse, response_model=APIOutput)
async def detect(request: Request, im: UploadFile):
    print(f"CPU Usage 2: {cpu_usage}%")
    print(im.filename)
    monitor_memory_usage()

    if im.filename.split('.')[-1] in ('jpg', 'jpeg', 'png'):
        pass

    else:
        raise HTTPException(
            status_code=415, detail='Not an Image'
        )

    # Read the uploaded image
    image = Image.open(BytesIO(await im.read()))
    print(f"CPU Usage 3: {cpu_usage}%")
    monitor_memory_usage()
    image = np.array(image)

    result_data = emotions_detector(image)
    print(f"CPU Usage 6: {cpu_usage}%")
    monitor_memory_usage()
    print(result_data)

    return templates.TemplateResponse("result.html", {"request": request, "result_data": result_data})

