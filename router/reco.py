from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
import pandas as pd
import pickle

from controller.repo.yield_apis_haru import YieldApi

router = APIRouter(
    prefix="/reco",
    responses={404: {"description": "Not found"}},
)


y = YieldApi()


@router.get("/yield")
async def reco_crops_yield(district, response:Response):

    data = pd.read_csv('./data/compiled_yield_data.csv')
    dist = data[data['District'] == district.upper()]
    dist.set_index("Year", inplace=True)
    dist = dist.drop(["District"], axis=1)

    scores = {}
    for(columnName, columnData) in dist.items():
        scores[columnName] = columnData.loc[2079] + (columnData.loc[2079]-columnData.loc[2078]) + (columnData.loc[2078]-columnData.loc[2077]) + (columnData.loc[2077]-columnData.loc[2076])

    scores_ordered = sorted(scores.items(), key=lambda x:x[1], reverse=True)
    crops = []
    crops.append(scores_ordered[0][0].split('_')[0])
    crops.append(scores_ordered[1][0].split('_')[0])
    crops.append(scores_ordered[2][0].split('_')[0])
    crops.append(scores_ordered[3][0].split('_')[0])

    result = []
    for crop in crops:
        crop_details = {}
        crop_details['crop'] = crop
        crop_details['yield'] = y.yearly_yield(district=district, crop=crop)
        crop_details['national_rank'] = y.national_rank(district=district, crop=crop)
        result.append(crop_details)

    # print(result)

    return JSONResponse(result)



@router.get('/soil')
async def reco_crops_soil(N, P, K, pH, response:Response):
    NB_pkl = open('./controller/naive_bayes_classifier.pkl', 'rb')
    NB_model = pickle.load(NB_pkl)

    curr_soil = {}
    curr_soil['N'] = N
    curr_soil['P'] = P
    curr_soil['K'] = K
    curr_soil['pH'] = pH


    df = pd.DataFrame(curr_soil, columns=['N','P','K','pH'], index=[0])

    crop = NB_model.predict(df)[0]
    result = {}
    result['crop'] = crop
    result['soil'] = y.soil_profile(crop=crop)
    return JSONResponse(result)




@router.get("/price")
async def reco_crops_yield(response:Response):

    data = pd.read_csv('./data/price.csv')
    price_data = data.loc[data['Unit']=='LCU']
    price_data = price_data.drop(['Element', 'year Code', 'Unit', 'Unit'],axis=1)

    # sort by the price for the recent year only --for now
    price_data = price_data[price_data['year']==2022]
    sorted_price = price_data.sort_values(by='value', ascending=False)

    crops = []
    crops.append(sorted_price.iloc[0]['Item'])
    crops.append(sorted_price.iloc[1]['Item'])
    crops.append(sorted_price.iloc[2]['Item'])
    crops.append(sorted_price.iloc[3]['Item'])

    result = []
    for crop in crops:
        crop_details = {}
        crop_details['crop'] = crop
        crop_details['price'] = y.get_price_data(crop=crop)
        result.append(crop_details)
    

    return JSONResponse(result)