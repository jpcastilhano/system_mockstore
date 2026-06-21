from fastapi import FastAPI

app = FastAPI(title="Mockstore API")


@app.get("/health")
def health_check():
    return {"status": "ok"}