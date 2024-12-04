from fastapi import APIRouter
from utils.analysis import perform_analysis

router = APIRouter()

@router.post("/perform-analysis")
def analyze_data():
    """Endpoint to analyze the dataset and create features."""
    input_path = "data/processed_data.csv"
    output_path = "outputs/results.csv"
    path = perform_analysis(input_path, output_path)
    return {"message": "Analysis completed successfully", "path": path}
