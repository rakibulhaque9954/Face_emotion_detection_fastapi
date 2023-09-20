import cv2
import numpy as np
import onnxruntime as rt
import time
import service.main as main


def emotions_detector(img_array):
    time_init = time.time()  # time started for calculating inference time

    # Converting image to np array and resizing for the model/preprocessing
    image = img_array
    image = cv2.resize(image, (256, 256))
    im = np.float32(image)
    im = np.expand_dims(im, axis=0)
    time_elapsed_preprocessing = f'{time.time() - time_init:.4f} secs'

    # Inference by passing the image to the model
    onnx_pred = main.model.run(['dense'], {'input_image': im})
    time_elapsed = f'{time.time() - time_init:.4f} secs'
    print(np.argmax(onnx_pred[0][0]))

    class_names = ['angry', 'happy', 'neutral', 'sad', 'surprised']
    emotion = class_names[np.argmax(onnx_pred[0][0])]

    return {'emotion': emotion,
            'time_elapsed_preprocessing': str(time_elapsed_preprocessing),
            'time_elapsed': str(time_elapsed)
             }
