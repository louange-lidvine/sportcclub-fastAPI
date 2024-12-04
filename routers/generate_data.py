from fastapi import APIRouter
from utils.generate_data import generate_data

router = APIRouter()

@router.get("/generate-data")
def generate_synthetic_data(rows: int = 500000):
    """Endpoint to generate synthetic data."""
    path = generate_data(rows=rows)
    return {"message": "Data generated successfully", "path": path}
