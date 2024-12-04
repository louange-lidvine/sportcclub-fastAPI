from fastapi import APIRouter
from utils.preprocess import preprocess_data

router = APIRouter()

@router.post("/preprocess-data")
def preprocess_dataset():
    """Endpoint to preprocess the dataset."""
    input_path = "data/raw_data.csv"
    output_path = "data/processed_data.csv"
    path = preprocess_data(input_path, output_path)
    return {"message": "Data preprocessed successfully", "path": path}
