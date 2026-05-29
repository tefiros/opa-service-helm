from fastapi import FastAPI

app = FastAPI()

@app.get("/example")
def example():
    return {"message": "todo okey"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)

