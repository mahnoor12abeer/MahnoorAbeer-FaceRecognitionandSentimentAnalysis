# Face Recognition and Emotion Analysis API
This project implements a face detection, recognition, and tracking system, alongside real-time sentiment analysis on faces in a virtual meeting video environment. The sentiment analysis classifies facial attributes into seven emotions: anger, fear, neutral, sad, disgust, happy, and surprise. Furthermore, the project is equipped with a REST API server, implemented using FastAPI, that performs the aforementioned analyses on uploaded videos.
## Features

- Face Detection and Recognition: Identifies and tracks faces in a virtual meeting video.
- Emotion Analysis: Performs real-time sentiment analysis on the detected faces, classifying emotions into seven categories.
- REST API Server: Provides an endpoint to upload videos for performing face and emotion analysis.

## Technology Stack

- FastAPI for creating REST API
- Docker for containerization
- PyTorch and Facenet-Pytorch for face detection
- DeepFace for emotion analysis
- Sort Algorithm for tracking

## Getting Started

### Prerequisites

- Docker
- Docker-compose

### Installation
1. Clone the repository:
   
```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd <project-directory>
```

3. Build and run the Docker container:

```bash
docker-compose up --build
```

### Usage

Once the docker container is up and running, the FastAPI server will be accessible at:

```url
http://0.0.0.0:5000
```

Navigate to this URL in your web browser. You will be presented with an interface to upload a video for analysis. The system will process the video, perform face detection, recognition, tracking, and emotion analysis, and then display the results.

### API Endpoints

- **GET /**: Displays the video upload page.
- **POST /**: Endpoint for uploading videos. Accepts video files and initiates processing.
- **GET /stream**: Returns a stream of the processed video with detected faces, recognition, tracking, and emotion analysis overlay.
- **GET /video_feed**: A continuous feed of the processed video frames.
- **GET /stop**: Endpoint to stop the server.

## Implementation References

This project utilizes the [SORT algorithm](https://github.com/abewley/sort) for real-time tracking and [DeepFace](https://github.com/serengil/deepface) for emotion analysis:

- SORT: A Simple, Online and Realtime Tracker used for tracking the detected faces across video frames.
- DeepFace: A deep learning model that provides facial attribute analysis algorithms including emotion detection.

Both tools have been integrated and modified as per the requirements of this project to work seamlessly with the FastAPI implementation and Docker environment.
## Acknowledgements

- [SORT algorithm](https://github.com/abewley/sort) by Alex Bewley
- [DeepFace](https://github.com/serengil/deepface) by Sefik Ilkin Serengil

Feel free to reach out for any questions or suggestions to improve this project.
