from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from ultralytics import YOLO
import shutil
import os
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load the trained model
MODEL_PATH = "best.pt"
try:
    model = YOLO(MODEL_PATH)
    logger.info(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise RuntimeError("Model loading failed.")

# Base directory for the application
BASE_DIR = Path(__file__).resolve().parent

# Directory to store input and output files
UPLOAD_DIR = BASE_DIR / "uploads"
RESULT_DIR = BASE_DIR / "results"

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)

# Mount the results directory for static file access
app.mount("/results", StaticFiles(directory=RESULT_DIR), name="results")


@app.get("/")
async def root():
    """
    Root endpoint to display API usage instructions.
    """
    return {"message": "Welcome to the YOLOv11 Detection API. Use /predict/ to perform inference."}


@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint to perform object detection on an uploaded image.
    """
    try:
        # Validate file type
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(
                status_code=400,
                detail="Invalid file type. Only JPEG and PNG are supported."
            )

        # Save uploaded file
        input_path = UPLOAD_DIR / file.filename
        with open(input_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logger.info(f"File uploaded successfully: {input_path}")

        # Perform inference
        output_path = RESULT_DIR / file.filename
        results = model.predict(source=str(input_path), save=True, save_dir=str(RESULT_DIR))

        logger.info(f"Detection completed. Results saved at: {output_path}")

        # Prepare detections
        detections = [
            {
                "label": res.boxes.cls.tolist(),
                "coordinates": res.boxes.xyxy.tolist(),
                "confidence": res.boxes.conf.tolist()
            } for res in results
        ]

        return JSONResponse(
            {
                "message": "Prediction completed successfully.",
                "input_file": str(input_path),
                "output_file": f"http://127.0.0.1:8000/results/{file.filename}",
                "detections": detections
            }
        )
    except HTTPException as e:
        logger.error(f"Error during prediction: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return JSONResponse({"error": str(e)}, status_code=500)
