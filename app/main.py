from fastapi import FastAPI

app = FastAPI()

students ={
    1:{
        "name": "john",
        "age": 17,
        "class": "B" }
    }


@app.get("/")
async def root():
    return {"name": "First Data"}