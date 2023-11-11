# Face Emotion Detection (FastAPI)

Welcome to my Face Emotion Detection project! This application is designed to detect emotions in faces from uploaded images using a combination of Haar Cascade for face detection and a ViT (Vision Transformer) model for emotion prediction. The model has been trained on 5 emotion classes: Happy, Sad, Angry, Surprised, and Neutral.

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

## Deployment

This project is hosted on Render, which may impact loading times and stability. Due to the nature of web applications, occasional crashes or slower response times may occur.

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
