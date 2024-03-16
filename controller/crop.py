import pandas as pd

yield_df = pd.read_csv('data/compiled-yield-data.csv')
soil_df = pd.read_csv('data/soil-profile.csv')
weather_df = pd.read_csv('data/weather-profile.csv')
price_df = pd.read_csv('data/price.csv')




def get_yields(district:str, crop:str):
    '''
    Get the total yields over the years of the required crop in the district provided

    Parameters:
    district (str): Name of the district
    crop (str): Name of the crop

    Returns:
    yields (list) : List of each years yield of the crop
    '''

    district = district.upper()
    crop = crop.lower() 
    crop_yield = crop + "_yield"

    crop_data = yield_df.loc[(yield_df['District']==district)]
    crop_yearly_data = crop_data.loc[:, ['Year', crop_yield]]

    years = [2076, 2077, 2078, 2079]
    yearly_crop_yield = []
    for year in years:
        crop_yields = crop_yearly_data.loc[crop_yearly_data['Year']==year, ['Year', crop_yield]]
        year_data = int(crop_yields.loc[:, 'Year'])
        yield_data = float(crop_yields.loc[:, crop_yield])
        yearly_crop_yield.append({
            'year' : year_data,
            'yield' : yield_data
        })
        
        # print(yearly_crop_yield)
    return yearly_crop_yield


def get_national_rank(district:str, crop:str):
    '''
    Get the national rank of the district on the basis of the yield of the required crop

    Parameters:
    district (str): Name of the district
    crop (str): Name of the crop

    Returns:
    national_rank (int) : Integer representing the rank of the district
    '''

    district  = district.upper()
    crop = crop.lower()
    crop = crop + "_yield"
    
    latest = yield_df.loc[(yield_df['Year']==2079)]               
    rank_data = 0

    sorted = latest.sort_values(crop, ascending = False)
    sorted = sorted.assign(row_num=range(len(sorted)))
    
    district_data = pd.DataFrame(sorted.loc[(sorted['District']==district)])  
    rank_value = int(district_data['row_num'])+1
    rank_data = rank_value
    
    return rank_data


def get_soil_profile(crop:str): 
    '''
    Get the average soil profile values ( N, P, K, pH ) that is optimal for the required crop

    Parameters:
    crop (str): Name of the crop

    Returns:
    soil_profile (dict[str, int | float]) : Dictionary with keys of N, P, K, pH and the corresponding average values
    '''
     
    crop = crop.lower()
    crop_soil = soil_df.loc[soil_df['Crop']==crop]

    soil_profile = {}
    soil_profile['N'] = round(crop_soil.loc[:,'N'].mean(),1)
    soil_profile['P'] = round(crop_soil.loc[:, 'P'].mean(),1)
    soil_profile['K'] = round(crop_soil.loc[:, 'K'].mean(),1)
    soil_profile['pH'] = round(crop_soil.loc[:, 'pH'].mean(),1)

    # print(soil_profile)
    return soil_profile


def get_weather_profile(crop:str):
    '''
    Get the optimal minimum and maximum values of weather parameters ( temperature, rainfall, humidity ) of the required crop

    Parameters:
    crop (str): Name of the crop

    Returns:
    weather_profile (dict[str, list]) : Dictionary with keys of temperature, rainfall, humidity containing corresponding min-max values in a list
    '''

    crop = crop.lower()
    crop_weather = weather_df.loc[weather_df['label']==crop]

    temp_max = round(crop_weather.loc[:,'temperature'].max(),1)
    temp_min = round(crop_weather.loc[:,'temperature'].min(),1)
    rain_max = round(crop_weather.loc[:,'rainfall'].max(),1)
    rain_min = round(crop_weather.loc[:,'rainfall'].min(),1)
    hum_max = round(crop_weather.loc[:,'humidity'].max(),1)
    hum_min = round(crop_weather.loc[:,'humidity'].min(),1)

    weather = {}
    weather['temperature'] = [temp_min, temp_max]
    weather['rainfall'] = [rain_min, rain_max]
    weather['humidity'] = [hum_min, hum_max]
    
    return weather   


def get_prices(crop:str):
    '''
    Get the yearly prices of the required crop

    Parameters:
    crop (str): Name of the crop

    Returns:
    prices (list) : A list of dicts each containing year and price of the crop
    '''

    crop = crop.lower() 

    crop_data = price_df.loc[(price_df['Item']==crop) & (price_df['Unit']=='LCU')]
    crop_yearly_data = crop_data.loc[:, ['year','value']]
    crop_yearly_data = crop_yearly_data.sort_values(by = ['year'])
    prices = crop_yearly_data.to_dict("records")
    
    # print(prices)
    return prices

