from fastapi import FastAPI

app = FastAPI()

@app.get("/2019")
async def index():
    return {"2019":"df2019dicc"}

@app.get("/2020")
async def index():
    return {"2020":"df2020dicc"}

@app.get("/2021")
async def index():
    return {"2021":"df2021dicc"}