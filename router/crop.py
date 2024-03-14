from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from controller.repo.yield_apis_haru import YieldApi


router = APIRouter(
prefix="/crop",
responses={404: {"description": "Not found"}},
)

y = YieldApi()
#1st - /crop/crop_name?district=query_param
'''
{yield: {2079: yield_value, 2078:7.8, 2077:2.6, 2076:6},
national_rank: 2,
soil: {
    N:avg(n_value),
    P:avg(),
    K:avg()
    pH:avg()
},
weather: {
    temperature: [min_value, max_value] #eg: [20.3, 26.6] - one decimal place,
    humidity: [min_value, max_value]- one decimal place,
    rainfall: [min_value, max_value] - no decimal
},
price:{2079: price_value, 2078:7.8, 2077:2.6, 2076:6, ............} all years 10 years back 
}  
'''





@router.get("/{crop}")
async def crop_page_yield(district, crop, response:Response):
    if district is None:
        return response.status_code== 404
    result = y.crop_page_api(district, crop)
    return JSONResponse(result)

