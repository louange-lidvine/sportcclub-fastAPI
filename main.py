from fastapi import FastAPI

from core.database import create_db_tables
# from routers.facilities import router as facilities_router
from routers.events import router as events_router
from routers.users import router as users_router
from routers import generate_data, preprocess, analysis

app = FastAPI()

# Function to create tables
@app.on_event("startup")
def create_tables():
    print("Tables are being created successfully")
    create_db_tables()


app.include_router(users_router)
# app.include_router(facilities_router,prefix="/facilities",tags=["facilities"])
app.include_router(events_router,prefix="/events",tags=["events"])

# app.include_router(events_router,prefix="/analytics",tags=["analytics"])
app.include_router(generate_data.router, prefix="/data", tags=["Data Generation"])
app.include_router(preprocess.router, prefix="/data", tags=["Preprocessing"])
app.include_router(analysis.router, prefix="/data", tags=["Analysis"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Data Pipeline"}
