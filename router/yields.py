from fastapi import APIRouter
from raw_datas.clean_data import ABC
from controller.repo.district_detail import YieldData
from yield_api import ApiFunctions

yd = YieldData()
d = ABC()
router = APIRouter(
prefix="/yields",
responses={404: {"description": "Not found"}},
)

yield_ko_api = ApiFunctions()



@router.get("/")
async def district_yield_detail(district):
    district_u = district.upper()
    result = yd.district_wise_latest_year_yield(district=district_u)
    return result

@router.get("/top_yields/")
async def district_top_yield(district):
    result = yield_ko_api.current_top_4_crops_district_wise(district)
    return result


@router.get("/top_yields_detail/")
async def district_top_yield_detail(district):
    result = yield_ko_api.change_in_percent(district)
    return result

