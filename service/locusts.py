from locust import SequentialTaskSet, HttpUser, task

class DetectorTask(SequentialTaskSet):
    @task
    def detection(self):
        with open('service/test_image.jpg', 'rb') as image:
            self.client.post(
                '/detect',
                files={'im': image}
            )

class LoadTester(HttpUser):
    host = 'https://rakibuls-emotion-detection-model.onrender.com'
    tasks = [DetectorTask]


# http://127.0.0.1:8089 this is the actual host link