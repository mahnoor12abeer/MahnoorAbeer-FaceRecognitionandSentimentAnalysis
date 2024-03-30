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
