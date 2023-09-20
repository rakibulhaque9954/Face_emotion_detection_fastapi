import cv2
import numpy as np
import time
import service.main as main


def emotions_detector(img_array):
    time_init = time.time()  # time started for calculating inference time

    # Load the Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Converting image to np array
    image = img_array

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    emotions = []

    for (x, y, w, h) in faces:
        # Crop and resize the face region for the model/preprocessing
        face = image[y:y + h, x:x + w]
        face = cv2.resize(face, (256, 256))
        im = np.float32(face)
        im = np.expand_dims(im, axis=0)

        # Inference by passing the face to the model
        onnx_pred = main.model.run(['dense'], {'input_image': im})

        # Predict emotion
        class_names = ['angry', 'happy', 'neutral', 'sad', 'surprised']
        emotion = class_names[np.argmax(onnx_pred[0][0])]
        emotions.append(emotion)

    time_elapsed_preprocessing = f'{time.time() - time_init:.4f} secs'
    time_elapsed = f'{time.time() - time_init:.4f} secs'

    return {'emotion': emotions,
            'time_elapsed_preprocessing': str(time_elapsed_preprocessing),
            'time_elapsed': str(time_elapsed)
            }
