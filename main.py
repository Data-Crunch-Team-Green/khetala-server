from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from router import yields, crop
# from controller.repo.district_detail import YieldData
# yd = YieldData()

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins= ['*'],
                   allow_credentials = True,
                   allow_methods = ['*'],
                   allow_headers= ['*']
                   )

app.include_router(yields.router)
app.include_router(crop.router)

@app.get("/")
async def root():
    return {"message": "Alive"}


@app.get("/app")
async def root():
    return FileResponse('data/compiled_yield_data.csv')



