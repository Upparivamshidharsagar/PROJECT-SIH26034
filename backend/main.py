from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Revenue Recovery Agent Backend is running"}