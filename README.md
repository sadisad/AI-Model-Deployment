# AI-Model-Deployment

## YOLOv11l Detection API

This repository contains a FastAPI-based application for object detection using the YOLOv11l model. The application allows users to upload images, perform object detection, and serve the results via a static directory.

---

## Features
- **Model:** YOLOv11l for accurate and efficient object detection.
- **API:** RESTful API endpoints for image upload and detection.
- **Dockerized:** Fully containerized application for easy deployment.
- **Static Results:** Annotated images are saved and accessible through a static file server.

---

## Quickstart

### 1. Prerequisites
Ensure you have the following installed:
- Python 3.11+
- Docker and Docker Compose
- Uvicorn (for local testing)

### 2. Installation

Ensure you have the following installed:

- Python 3.11+
- Docker and Docker Compose
- Uvicorn (for local testing)

### 2. Installation

1. Clone the repository:

- git clone <repository-url>
- cd <repository-directory>

2. Install dependencies:

- pip install -r requirements.txt

3. Run the application locally:

- uvicorn app:app --host 0.0.0.0 --port 8000

### Docker Deployment

1. Build the Docker image:

- docker build -t yolo-inference .

2. Run the Docker container:

- docker run --rm -p 8000:8000 -v $(pwd)/uploads:/app/uploads -v $(pwd)/results:/app/results yolo-inference

3. Access the API:

- Root endpoint: http://127.0.0.1:8000/

- Predict endpoint: http://127.0.0.1:8000/predict/

## API Endpoints

- GET /

Displays API usage instructions.

- POST /predict/

Uploads an image and performs object detection.

Request:

* File: An image file (JPEG or PNG).

Response:

* JSON object with:

  * input_file: Path to the uploaded file.

  * output_file: URL to the annotated image.

  * detections: List of detected objects with labels, coordinates, and confidence scores.

## Directory Structure

/app
├── app.py          # Main application file
├── uploads/        # Directory for uploaded files
├── results/        # Directory for annotated files
├── requirements.txt # Python dependencies
├── Dockerfile      # Dockerfile for containerization

## Example Usage

### Using Postman

1. Open Postman and create a new POST request.

2. Set the request URL to:

http://127.0.0.1:8000/predict/

3. In the Body tab, select form-data and add the following key-value pair:

Key: file

Value: Select an image file (JPEG or PNG) from your local machine.

4. Send the request and view the response.

5. Access the annotated image at the output_file URL provided in the response.

### Using curl

1. Upload an image to /predict/ using the following command:

curl -X POST "http://127.0.0.1:8000/predict/" -F "file=@path_to_image.jpg"

2. View the result at the provided output_file URL.

## Testing

To ensure the application is functioning correctly:

1. Run the application locally or in Docker.

2. Upload sample images and verify detections.

3. Monitor performance metrics (CPU, memory usage).

## Future Improvements

1. Optimize Docker image size using Alpine base image.

2. Convert the model to ONNX/TensorRT for faster inference.

3. Automate deployment using CI/CD pipelines.

4. Add GPU support for enhanced performance.

## License

This project is licensed under the MIT License.

