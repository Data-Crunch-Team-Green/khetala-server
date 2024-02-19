from fastapi import FastAPI
from router import yields


app = FastAPI()

app.include_router(yields.router)

@app.get("/")
async def root():
    return {"message": "Alive"}

