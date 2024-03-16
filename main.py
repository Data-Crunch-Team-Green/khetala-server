from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import crop, reco

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins= ['*'],
                   allow_credentials = True,
                   allow_methods = ['*'],
                   allow_headers= ['*']
                   )

app.include_router(crop.router)
app.include_router(reco.router)

@app.get("/")
async def root():
    return {"message": "Alive"}



