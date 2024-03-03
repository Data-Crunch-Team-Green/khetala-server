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




@router.get("/top_4_yields/")
async def district_top_yield(district):
    result = yield_ko_api.top_4_crops_district_wise(district)
    return result

@router.get("/top_4_yields_percent_change/")
async def district_top_yield_percent_change(district):
    result = yield_ko_api.top_4_crops_percent_change(district)
    return result

@router.get("/top_4_yields_national_rank/")
async def district_top_yield_ranks(district):
    result = yield_ko_api.top_4_crops_national_rank(district)
    return result

@router.get("/district_overall_crop_yield/")
async def district_yearly_crop_yields(district, crop):
    result = yield_ko_api.overall_yields_of_district_wise_crop(district, crop)
    return result

@router.get("/percent_change_crop/")
async def percent_change_crop_yields(district, crop):
    result = yield_ko_api.change_in_percent_crop_and_district_wise(district, crop)
    return result

@router.get("/district_with_highest_yield/")
async def district_with_highest_yield(crop):
    result = yield_ko_api.district_with_highest_yield_in_the_nation(crop)
    return result