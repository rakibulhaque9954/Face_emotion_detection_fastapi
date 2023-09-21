from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
import numpy as np
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from service.core.logic.onnx_inference import emotions_detector
from service.core.schemas.output import APIOutput
from fastapi import Request

detect_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@detect_router.post('/detect', response_class=HTMLResponse, response_model=APIOutput)
async def detect(request: Request, im: UploadFile):
    if im.filename.split('.')[-1] in ('jpg', 'jpeg', 'png'):
        pass

    else:
        raise HTTPException(
            status_code=415, detail='Not an Image'
        )

    # Read the uploaded image
    image = Image.open(BytesIO(await im.read()))
    image = np.array(image)

    result_data = emotions_detector(image)
    print(result_data)

    return templates.TemplateResponse("result.html", {"request": request, "result_data": result_data})

