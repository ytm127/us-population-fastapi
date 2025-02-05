from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
async def root():
    res = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    return {"message": res.json()}
