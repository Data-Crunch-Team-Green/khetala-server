from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
import pandas as pd
import pickle

from controller.crop import get_yields, get_national_rank, get_soil_profile, get_prices

router = APIRouter(
    prefix="/recommend",
    responses={404: {"description": "Not found"}},
)


@router.get("/yield")
async def recommend_crops_by_yield(district, response:Response):

    data = pd.read_csv('./data/compiled-yield-data.csv')
    dist = data[data['District'] == district.upper()]
    dist.set_index("Year", inplace=True)
    dist = dist.drop(["District"], axis=1)

    # calculate a score from yield performance over the 4 years
    # the crops will be ranked based on this score and top four will be recommended
    # TODO: create separate util function to calculate score using the values of the parameter (yield like here) over the years. This function could be used in the recommendation by price below

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
        crop_details['yield'] = get_yields(district, crop)
        crop_details['national_rank'] = get_national_rank(district, crop)
        result.append(crop_details)

    # print(result)

    return JSONResponse(result)



@router.get('/soil')
async def recommend_crops_by_soil(N, P, K, pH, response:Response):
    NB_pkl = open('./src/model_ml/naive_bayes_classifier.pkl', 'rb')
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
    result['soil'] = get_soil_profile(crop)

    return JSONResponse(result)




@router.get("/price")
async def recommend_crops_by_price(response:Response):

    data = pd.read_csv('./data/price.csv')
    price_data = data.loc[data['Unit']=='LCU']
    price_data = price_data.drop(['Element', 'year Code', 'Unit', 'Unit'],axis=1)

    # sorting the crop by the price for the recent year only --for now
    # might be better to calculate the score and sort by the score as the yields above

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
        crop_details['price'] = get_prices(crop=crop)
        result.append(crop_details)

    return JSONResponse(result)