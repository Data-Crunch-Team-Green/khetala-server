from fastapi import APIRouter, Response, HTTPException
from fastapi.responses import JSONResponse

from controller.crop import get_yields, get_national_rank, get_soil_profile, get_weather_profile, get_prices


router = APIRouter(
prefix="/crop",
tags=['crop'],
responses={404: {"description": "Not found"}},
)


@router.get("/{crop_name}")
async def get_crop_details(district, crop_name, response:Response):
    # TODO: is there a better way of handling bad requests
    if district is None:
        raise HTTPException(status_code=400, detail="Name of a district is required")
    
    result ={}
    result['crop'] = crop_name
    result['district'] = district
    result['national_rank'] = get_national_rank(district, crop=crop_name)
    result['yield'] = get_yields(district, crop=crop_name)
    result['soil'] = get_soil_profile(crop=crop_name)
    result['weather'] = get_weather_profile(crop=crop_name)
    result['price'] = get_prices(crop=crop_name)

    return JSONResponse(result)

