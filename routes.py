from fastapi import APIRouter
from services.processor import HighPerformanceProcessor

router = APIRouter()

processor = HighPerformanceProcessor()

@router.get("/")
def home():
    return {"message": "High Performance App Running"}

@router.post("/process")
async def process_data(data: list[str]):

    results = await processor.process_concurrently(data)

    return {
        "processed_results": results
    }