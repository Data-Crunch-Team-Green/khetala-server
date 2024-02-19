from fastapi import APIRouter




router = APIRouter(
prefix="/yield",
tags=["yield"],
responses={404: {"description": "Not found"}},
)



@router.get("/")
async def read_users():
    return "maya"
