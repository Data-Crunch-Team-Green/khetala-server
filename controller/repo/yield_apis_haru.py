import pandas as pd
import json
import numpy as np 

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

class YieldApi:

    yield_data = pd.read_csv('data/compiled_yield_data.csv')
    soil_data = pd.read_csv('data/fertilizer.csv')
    weather_data = pd.read_csv('data/cpdata2.csv')
    price_data = pd.read_csv('data/price.csv')

    def yearly_yield(self, district:str, crop:str) -> json:
        district = district.upper()
        crop = crop.lower() 
        crop_yield = crop + "_yield"
        combined_data = self.yield_data   
        yield_data_df = pd.DataFrame(combined_data)

        crop_data = yield_data_df.loc[(yield_data_df['District']==district)]
        crop_yearly_data = crop_data.loc[:, ['Year', crop_yield]]

        years = [2076, 2077, 2078, 2079]
        yearly_crop_yield = []
        for year in years:
            crop_yields = crop_yearly_data.loc[crop_yearly_data['Year']==year, ['Year', crop_yield]]
            df_crop_yield = pd.DataFrame(crop_yields)
            year_data = int(df_crop_yield.loc[:, 'Year'])
            yield_data = float(df_crop_yield.loc[:, crop_yield])
            yearly_crop_yield.append({
                'year' : year_data,
                'yield' : yield_data
            })
         
            print(yearly_crop_yield)
        return yearly_crop_yield


    def national_rank(self, district:str, crop:str) -> json:
        district  = district.upper()
        crop = crop.lower()
        crop = crop + "_yield"
        yield_data = self.yield_data
        yield_data_df = pd.DataFrame(yield_data)
       
        latest = yield_data_df.loc[
            (yield_data_df['Year']==2079)
            ]               
        rank_data = 0

        sorted = latest.sort_values(crop, ascending = False)
        sorted = sorted.assign(row_num=range(len(sorted)))
        
        district_data = pd.DataFrame(sorted.loc[(sorted['District']==district)])  
        rank_value = int(district_data['row_num'])+1
        rank_data = rank_value

      
        return rank_data
                

    def soil_profile(self, crop:str) -> json: 
     
        crop = crop.lower()
        soil_data = pd.DataFrame(self.soil_data)
        crop_soil = soil_data.loc[soil_data['Crop']==crop]
        Ni = round(crop_soil.loc[:,'N'].mean(),1)
        Po = round(crop_soil.loc[:, 'P'].mean(),1)
        Ko = round(crop_soil.loc[:, 'K'].mean(),1)
        pH = round(crop_soil.loc[:, 'pH'].mean(),1)
        soil = {}
        soil['N'] = Ni
        soil['P'] = Po
        soil['K'] = Ko
        soil['npk'] = [
            {
            'label': 'N',
            'value': Ni
            },
            {
            'label': 'P',
            'value': Po
            },
            {
            'label': 'K',
            'value': Ko
            },
        ]
        soil['pH'] = pH
        # print(soil)
        return soil
    

    def get_weather_data(self, crop:str) -> json:
        weather_data = pd.DataFrame(self.weather_data)
        crop = crop.lower()
        crop_weather = weather_data.loc[weather_data['label']==crop]
        temp_max = round(crop_weather.loc[:,'temperature'].max(),1)
        temp_min = round(crop_weather.loc[:,'temperature'].min(),1)
        rain_max = round(crop_weather.loc[:,'rainfall'].max(),1)
        rain_min = round(crop_weather.loc[:,'rainfall'].min(),1)
        hum_max = round(crop_weather.loc[:,'humidity'].max(),1)
        hum_min = round(crop_weather.loc[:,'humidity'].min(),1)

        weather = {}
        temp = []
        rainfall = []
        humidity = []

        temp.append(temp_min)
        temp.append(temp_max)
        rainfall.append(rain_min) 
        rainfall.append(rain_max)
        humidity.append(hum_min)
        humidity.append(hum_max)

        weather['temperature'] = temp
        weather['rainfall'] = rainfall
        weather['humidity'] = humidity
        
        return weather   



    def get_price_data(self,  crop) -> json:

        crop = crop.lower() 
       
        yield_data_df = pd.DataFrame(self.price_data)

        crop_data = yield_data_df.loc[(yield_data_df['Item']==crop) & (yield_data_df['Unit']=='LCU')]
        crop_yearly_data = crop_data.loc[:, ['year','value']]
        crop_yearly_data = crop_yearly_data.sort_values(by = ['year'])
        d = crop_yearly_data.to_dict("records")
      
        return d

        # print(d)
        







    def crop_page_api(self, district , crop):
        result = {}
        yield_data = self.yearly_yield(district=district, crop=crop)
        national_rank = self.national_rank(district=district, crop=crop)
        soil_profile_data = self.soil_profile(crop=crop)
        weather_data = self.get_weather_data(crop=crop)
        price_data = self.get_price_data(crop=crop)
        result['yield']= yield_data
        result['national_rank'] = national_rank
        result['soil'] = soil_profile_data
        result['weather'] = weather_data
        result['price'] = price_data
        # print(result)
        return result
    
def lower(column):
        return column.lower()

def converting_lower_case( filepath:str, column_name, new_file_name):
    df = pd.DataFrame(pd.read_csv(filepath))
    column_change = df[column_name]
        
    lower_case_column = column_change.apply(lower)
    df[column_name]=lower_case_column
    df.to_csv(new_file_name, index = False)
    
    return df 

def divide(column):
    return round(column/1000,1)
def converting_kg_to_hc(filepath, crop_yield, file_name, year):
    df =  pd.DataFrame(pd.read_csv(filepath))
    filtered0 = df.loc[df['Year']==year]
    filtered = df.loc[:,[crop_yield,'District']]

    conversion = filtered.apply(divide)
    filtered[crop_yield]=conversion
    filtered.to_csv(file_name, index = False)
    return filtered



  



                    

if __name__ == "__main__":
    a = YieldApi()
    a.get_price_data(crop =  'Millet')
    # a.Spaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
    # a.Mpaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
    # a.yearly_yield(district= 'palpa', crop = 'tea') 
    # converting_lower_case(filepath='data/fertilizer.csv', column_name='Crop', new_file_name='fertilizer.csv' )
    converting_kg_to_hc('data/compiled_yield_data.csv', 'Jute_yield', 'jute.csv', '2076')
        
