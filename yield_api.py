from raw_datas.clean_data import ABC
import pandas as pd

from fastapi import APIRouter
import pandas as pd

d = ABC()

class ApiFunctions:
    
  
    def current_top_4_crops_district_wise(self,district):
        district = district.upper()
        dataset = d.final_2079_data()
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

    def change_in_percent(self, district):
        district  = district.upper()
        crops_to_look = self.current_top_4_crops_district_wise(district= district)
        yield_data = pd.read_csv('raw_datas/full_data.csv')
        print(yield_data)
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
        print(percent_data)
        return percent_data
               
             
               
                
                


if __name__ == '__main__':
    p = ApiFunctions()
    p.change_in_percent('dhankuta')
