from fastapi import FastAPI
from router import yields
from controller.repo.district_detail import YieldData

yd = YieldData()

app = FastAPI()

app.include_router(yields.router)

@app.get("/")
async def root():
    return {"message": "Alive"}

