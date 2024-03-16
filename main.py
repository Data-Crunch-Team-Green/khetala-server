from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import crop, recommend

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins= ['*'],
                   allow_credentials = True,
                   allow_methods = ['*'],
                   allow_headers= ['*']
                   )

app.include_router(crop.router)
app.include_router(recommend.router)

@app.get("/")
async def ping():
    return {"message": "Alive"}



