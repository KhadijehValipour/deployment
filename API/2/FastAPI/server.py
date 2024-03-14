from fastapi import FastAPI

app = FastAPI()

@app.get("/khadijeh")
def read_root():
    return {"Hello" : "World"}