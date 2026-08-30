from fastapi import FastAPI
from database.models import create_tables
from api.routes import router

app = FastAPI()
app.include_router(router)
create_tables()


@app.get("/")
def home():
    return {"message": "Revenue Recovery Agent Backend is running"}