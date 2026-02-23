from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()  # Load environment variables from .env file
from router import router  # Import the router from your router.py file
from db import Base, engine

# Initialize the FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include the router
app.include_router(router, prefix="/api", tags=["employees_details"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CRUD application!"}