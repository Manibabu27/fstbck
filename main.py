from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()  
from router import router  
from db import Base, engine
from fastapi.middleware.cors import CORSMiddleware 


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




origins = [ 
    "http://localhost:5173", 
# # React dev server "https://your-deployed-frontend.com"
 ] 
app.add_middleware( 
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"], 
)