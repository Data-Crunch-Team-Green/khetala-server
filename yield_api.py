from raw_datas.clean_data import ABC
import pandas as pd
import json
from fastapi import APIRouter
import pandas as pd

d = ABC()
class ApiFunctions:
  
    def top_4_crops_district_wise(self,district:str)-> list:
        district = district.upper()
        yield_data = pd.read_csv('raw_datas/full_data.csv')
        yield_data_df = pd.DataFrame(yield_data)
        dataset = yield_data_df.loc[
            (yield_data_df['Year']==2079)
            ]

        district_data = dataset[dataset["District"] == district]
        yield_columns = district_data.filter(like="_yield")
        top_yields = yield_columns.squeeze().nlargest(4)
        column_names = district_data.loc[:, top_yields.index].columns.tolist()
        datas = []
        for yield_value, column_name in zip(top_yields, column_names):
            a = {column_name: yield_value}
            datas.append(a)
        print(datas)
        return datas

    def top_4_crops_percent_change(self, district:str) -> list:
        district  = district.upper()
        crops_to_look = self.top_4_crops_district_wise(district= district)
        yield_data = pd.read_csv('raw_datas/full_data.csv')
        yield_data_df = pd.DataFrame(yield_data)

        row_2078 = yield_data_df.loc[(yield_data_df['Year']==2078)&(yield_data_df['District']==district)]
      
        percent_data = []
        for crop in crops_to_look:
            for key in crop.keys():
                row_2079 = yield_data_df.loc[(yield_data_df['Year']==2079)&(yield_data_df['District']==district)]
                df_2079= pd.DataFrame(row_2079)
                row_2078 = yield_data_df.loc[(yield_data_df['Year']==2078)&(yield_data_df['District']==district)]
                df_2078= pd.DataFrame(row_2078)
                value_2079 = float(df_2079.loc[:, key])
                value_2078 = float(df_2078.loc[:, key])
                percent_change = round(((value_2079- value_2078)/value_2078)*100,2)
                percent_data.append({key:percent_change})
       
        return percent_data
    
    def top_4_crops_national_rank(self, district:str) -> list:
        district  = district.upper()
        crops_to_look = self.top_4_crops_district_wise(district= district)

        yield_data = pd.read_csv('raw_datas/full_data.csv')
        yield_data_df = pd.DataFrame(yield_data)
       
        row_2079 = yield_data_df.loc[
            (yield_data_df['Year']==2079)
            ]
                
        rank_data = []

        for crop in crops_to_look:
            rank = 0
            for key in crop.keys():
                sorted = row_2079.sort_values(key, ascending = False)
                sorted = sorted.assign(row_num=range(len(sorted)))
                print(sorted)
                district_data =pd.DataFrame(sorted.loc[(sorted['District']==district)])        
                rank_value = int(district_data['row_num'])+1
                rank += rank_value
                rank_data.append({key:rank})

        print(rank_data)
        return rank_data
                
        

        


        """
        national rank
        crop wise 
        sort garna pryo
        then tyo key anusar tyo rank ko value
        year district barleyyield wheatyield
        """
          
    def overall_yields_of_district_wise_crop(self, district:str, crop:str)-> dict:
        district = district.upper()
        yield_data = pd.read_csv('raw_datas/full_data.csv')
        yield_data_df = pd.DataFrame(yield_data)
        yearly_data = yield_data_df.loc[
            (yield_data_df['District']== district)
        ]
        crop_yearly_data = yearly_data.loc[:, ['Year', 'District', crop]]

        years = [2076, 2077, 2078, 2079]
        yearly_crop_yield = {}
        for year in years:
            crop_yield = crop_yearly_data.loc[crop_yearly_data['Year']==year, ['Year', crop]]
            df_crop_yield = pd.DataFrame(crop_yield)
            year_data = int(df_crop_yield.loc[:, 'Year'])
            yield_data = float(df_crop_yield.loc[:, crop])
            yearly_crop_yield[year_data]=yield_data

        print(yearly_crop_yield)
        return yearly_crop_yield

    def change_in_percent_crop_and_district_wise(self, district:str, crop:str)-> dict:
        district  = district.upper()
        
        yield_data = pd.read_csv('raw_datas/full_data.csv')
        yield_data_df = pd.DataFrame(yield_data)

        row_2078 = yield_data_df.loc[(yield_data_df['Year']==2078)&(yield_data_df['District']==district)]
      
        percent_data = {}
   
        row_2079 = yield_data_df.loc[(yield_data_df['Year']==2079)&(yield_data_df['District']==district)]
        df_2079= pd.DataFrame(row_2079)
        row_2078 = yield_data_df.loc[(yield_data_df['Year']==2078)&(yield_data_df['District']==district)]
        df_2078= pd.DataFrame(row_2078)
        value_2079 = float(df_2079.loc[:, crop])
        value_2078 = float(df_2078.loc[:, crop])
        percent_change = round(((value_2079- value_2078)/value_2078)*100,2)
        percent_data[crop]= percent_change
        print(percent_data)
        return percent_data
                                    
    def district_with_highest_yield_in_the_nation(self, crop:str):

        yield_data = pd.read_csv('raw_datas/full_data.csv')
        yield_data_df = pd.DataFrame(yield_data)
       
        row_2079 = yield_data_df.loc[
            (yield_data_df['Year']==2079)
            ]
                
        top_district = ""

        sorted = row_2079.sort_values(crop, ascending = False)
        sorted = sorted.assign(row_num=range(len(sorted)))
        district_data =sorted.iloc[0,:]
        district_name = district_data['District']
        top_district+= district_name

        print(top_district)
        return top_district

# if __name__ == '__main__':
#     p = ApiFunctions()
#     # p.current_top_4_crops_district_wise('kathmandu')
#     # p.district_yearly_yield('bhaktapur', 'Paddy_main_yield')
#     # p.national_rank('dhankuta')
#     # p.change_in_percent_crop('jumla', 'Paddy_total_yield')
#     p.district_yield_highest_in_the_nation('Barley_yield')
