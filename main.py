from fastapi import FastAPI
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