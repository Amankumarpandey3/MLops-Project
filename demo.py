from src.logger import logging
from src.pipline.training_pipeline import TrainPipeline
from src.components.model_trainer import ModelTrainer
import os

# Verify MongoDB URL
mongodb_url = os.getenv("MONGODB_URL")
if not mongodb_url:
    raise EnvironmentError("MONGODB_URL environment variable is not set. Please set it before running the script.")
print("MONGODB_URL:", mongodb_url)

# Run the pipeline
pipeline = TrainPipeline()
try:
    pipeline.run_pipeline()
except Exception as e:
    logging.error(f"Pipeline execution failed: {e}")
    raise