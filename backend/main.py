
from fastapi import FastAPI

from backend.database.models import create_tables
from backend.api.routes import router

app = FastAPI()

app.include_router(router)

create_tables()

@app.get("/")
def home():
    return {"message": "Revenue Recovery Agent Backend is running"}