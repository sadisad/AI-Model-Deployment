# AI-Model-Deployment

YOLOv11l Detection API

This repository contains a FastAPI-based application for object detection using the YOLOv11l model. The application allows users to upload images, performs object detection, and serves the results via a static directory.

Features

Model: YOLOv11l for accurate and efficient object detection.

API: RESTful API endpoints for image upload and detection.

Dockerized: Fully containerized application for easy deployment.

Static Results: Annotated images are saved and accessible through a static file server.

Quickstart

Prerequisites

Ensure you have the following installed:

Python 3.11+

Docker and Docker Compose

Uvicorn (for local testing)

Installation

Clone the repository:

git clone <repository-url>
cd <repository-directory>

Install dependencies:

pip install -r requirements.txt

Run the application locally:

uvicorn app:app --host 0.0.0.0 --port 8000

Docker Deployment

Build the Docker image:

docker build -t yolo-inference .

Run the Docker container:

docker run --rm -p 8000:8000 -v $(pwd)/uploads:/app/uploads -v $(pwd)/results:/app/results yolo-inference

Access the API:

Root endpoint: http://127.0.0.1:8000/

Predict endpoint: http://127.0.0.1:8000/predict/

API Endpoints

GET /

Displays API usage instructions.

POST /predict/

Uploads an image and performs object detection.

Request:

File: An image file (JPEG or PNG).

Response:

JSON object with:

input_file: Path to the uploaded file.

output_file: URL to the annotated image.

detections: List of detected objects with labels, coordinates, and confidence scores.

Directory Structure

/app
├── app.py          # Main application file
├── uploads/        # Directory for uploaded files
├── results/        # Directory for annotated files
├── requirements.txt # Python dependencies
├── Dockerfile      # Dockerfile for containerization

Example Usage

Upload an image to /predict/ using a tool like Postman or curl:

curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@path_to_image.jpg"

View the result at the provided output_file URL.

Testing

To ensure the application is functioning correctly:

Run the application locally or in Docker.

Upload sample images and verify detections.

Monitor performance metrics (CPU, memory usage).

Future Improvements

Optimize Docker image size using Alpine base image.

Convert the model to ONNX/TensorRT for faster inference.

Automate deployment using CI/CD pipelines.

Add GPU support for enhanced performance.

License

This project is licensed under the MIT License.
