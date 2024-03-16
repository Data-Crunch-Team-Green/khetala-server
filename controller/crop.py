import pandas as pd

class Crop:
    yield_df = pd.read_csv('data/compiled_yield_data.csv')

    def get_yields(self, district:str, crop:str):
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
        combined_data = self.yield_df   
        # no need for this -- yield_df is already a dataframe
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
         
            # print(yearly_crop_yield)
        return yearly_crop_yield


    def get_national_rank(self, district:str, crop:str):
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
        yield_data = self.yield_df
        # no need to make dataframe here again
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
