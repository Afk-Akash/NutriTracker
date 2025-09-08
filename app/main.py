# main.py
from fastapi import FastAPI

app = FastAPI(title="CalorieTracker API")


@app.get("/")
def root():
    return {"message": "CalorieTracker API is running 🚀"}


# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
