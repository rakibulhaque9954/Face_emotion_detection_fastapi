# Face Emotion Detection (FastAPI)
[日本語](https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/135e72cc144661da34902d55e3643b1ae700abb9/%E6%97%A5%E6%9C%AC%E8%AA%9EREADME.md)
Welcome to my Face Emotion Detection project! This application is designed to detect emotions in faces from uploaded images using a combination of Haar Cascade for face detection and a ViT (Vision Transformer) model for emotion prediction. The model has been trained on 5 emotion classes: Happy, Sad, Angry, Surprised, and Neutral.

## Website Preview
![home page](https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/cde903776333edd143cc5f8a15da9dd704d452e7/Screenshot%202023-11-11%20at%2018.17.25.png)
*Home Page*
<br>
<img src="https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/cde903776333edd143cc5f8a15da9dd704d452e7/1000_F_637048304_gG1q9XoPsy17wtqm1rCM8ke3EjENcq5N.jpg" width="400" alt="Sample Happy Image"><br>
*Test Image(emotion: Happy)*
<br>
![Result](https://github.com/rakibulhaque9954/Face_emotion_detection_fastapi/blob/cde903776333edd143cc5f8a15da9dd704d452e7/Screenshot%202023-11-11%20at%2018.18.03.png)
*Result page*

## Usage

1. Upload an image containing a face.
2. The Haar Cascade algorithm will detect the face.
3. The image, converted to a numpy array, is then passed to the ViT Transformer model.
4. The model predicts the emotion of the detected face.

## Model Details

- I use a ViT Transformer model pretrained on Google's Patch 16 dataset with an image size of 224x224 pixels.
- The model is fine-tuned on a custom emotion dataset, which includes Kaggle's dataset and additional custom data, to accurately classify emotions.

## Adding Custom Dataset and Kaggle

To enhance model accuracy, I added a custom dataset that includes a combination of Kaggle's dataset and additional custom data. This expanded dataset allowed my model to better understand and classify a wider range of emotions.
**A val Accuracy of 90% was achieved.**

## Deployment

This project is hosted on Render, which may impact loading times and stability. Due to the nature of hosting service, occasional crashes or slower response times may occur.

## Technologies Used

- FastAPI: For building the web application.
- Haar Cascade: For face detection.
- Vision Transformer (ViT): For emotion prediction.
- Google's Patch 16 Dataset: For pretraining the ViT model.
- Kaggle Dataset: Incorporated for comprehensive training.

## Running the Application Locally

To run this application locally, follow these steps:

1. Clone this repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI app using `uvicorn app:app --reload`.

## Notebook Repository

Explore the project's development and model training in detail by visiting my notebook repository [here](https://github.com/rakibulhaque9954/Emotion_Detection_Model-ViT-_V1.0.git).

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [License](https://github.com/rakibulhaque9954/blog_remastered/blob/418d35cf33f0411375ed2dc77fc3607ee5887fc9/MIT_LICENSE_Rakibul_Haque.txt) file for details.

Enjoy exploring and using the Face Emotion Detection application!
