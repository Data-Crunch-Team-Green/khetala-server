
import pandas as pd 

class ABC:
    def json_to_df(self,path:str,  year:int):
        df = pd.read_json(path)
        df['Year'] = year
        reordered = df.iloc[:, [4,0,1,2,3]]
        return reordered

    def paddy_json_to_df(self,path:str,  year:int):
        df = pd.read_json(path)
        df['Year'] = year
        reordered = df.iloc[:, [4,0,1,2,3]]
        reordered = reordered.iloc[:,[0,1,4]]
        reordered = reordered.rename(columns = {'Total_yield': 'Paddy_total_yield'})
        print(reordered)
        return reordered
    
    
    def Spaddy_json_to_df(self,path:str,  year:int):
        df = pd.read_json(path)
        df['Year'] = year
        reordered = df.iloc[:, [4,0,1,2,3]]
        reordered = reordered.iloc[:,[0,1,2]]
        reordered = reordered.rename(columns = {'Spring_yield': 'Paddy_spring_yield'})
        return reordered

    def Mpaddy_json_to_df(self,path:str,  year:int):
        df = pd.read_json(path)
        df['Year'] = year
        reordered = df.iloc[:, [4,0,1,2,3]]
        reordered = reordered.iloc[:,[0,1,3]]
        reordered = reordered.rename(columns = {'Main_yield': 'Paddy_main_yield'})
        return reordered
    

    def joining_tables(self,t1, t2, t3, t4, t5, t6, t7, t8):
        table1 = pd.merge(t1, t2, on = ['District', 'Year'], how= 'inner')
        table2 = pd.merge(table1, t3, on = ['District', 'Year'], how= 'inner')
        table3 = pd.merge(table2, t4, on = ['District', 'Year'], how= 'inner')
        table4 = pd.merge(table3, t5, on = ['District', 'Year'], how= 'inner') 
        table5 = pd.merge(table4, t6, on = ['District', 'Year'], how= 'inner')
        table6 = pd.merge(table5, t7, on = ['District', 'Year'], how= 'inner')
        table7 = pd.merge(table6, t8, on = ['District', 'Year'], how= 'inner')

        return table7
    

    def joining_tables1(self,t1, t2):
        table1 = pd.merge(t1, t2, on = ['District', 'Year'], how= 'left')
        # table2 = pd.merge(table1, t3, on = ['District', 'Year'], how= 'inner')
        
 
        return table1
    

   


    def final_2079_data(self):
        barley_2079 = self.json_to_df('raw_datas/2079_data/barley_yield.json',  2079)
        maize_2079 = self.json_to_df('raw_datas/2079_data/maize_yield.json', 2079)
        buckwheat_2079 = self.json_to_df('raw_datas/2079_data/buckwheat_yield.json',  2079)
        millet_2079 = self.json_to_df('raw_datas/2079_data/millet_yield.json',  2079)
        wheat_2079 =  self.json_to_df('raw_datas/2079_data/wheat_yield.json',  2079)
        paddy_2079 =  self.paddy_json_to_df('raw_datas/2079_data/paddy_yield.json',  2079)
        s_paddy_2079 = self.Spaddy_json_to_df('raw_datas/2079_data/paddy_yield.json',  2079)
        m_paddy_2079 = self.Mpaddy_json_to_df('raw_datas/2079_data/paddy_yield.json',  2079)

        final_2079 = self.joining_tables(barley_2079, maize_2079, buckwheat_2079, millet_2079, wheat_2079, paddy_2079, s_paddy_2079, m_paddy_2079)

        final_2079.replace('-', 0, inplace=True)
        final_2079['Millet_yield'] = final_2079['Millet_yield'].astype(float)
        final_2079['Paddy_total_yield'] = final_2079['Paddy_total_yield'].astype(float)
        final_2079['Paddy_spring_yield'] = final_2079['Paddy_spring_yield'].astype(float)
        final_2079['Paddy_main_yield'] = final_2079['Paddy_main_yield'].astype(float)
        final_2079['Barley_yield'] = final_2079['Barley_yield'].astype(float)
        final_2079['Buckwheat_yield'] = final_2079['Buckwheat_yield'].astype(float)
        
        return final_2079

    def data_2078(self):
      
        barley_2078 = self.json_to_df('raw_datas/2078_data/barley_yield.json',  2078)
        maize_2078 = self.json_to_df('raw_datas/2078_data/maize_yield2078.json', 2078)
        buckwheat_2078 = self.json_to_df('raw_datas/2078_data/buckwheat_yield.json',  2078)
        millet_2078 = self.json_to_df('raw_datas/2078_data/millet_yield.json',  2078)
        wheat_2078 =  self.json_to_df('raw_datas/2078_data/wheat_yield2078.json',  2078)
        paddy_2078 =  self.paddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
        s_paddy_2078 = self.Spaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
        m_paddy_2078 = self.Mpaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
        final_2078 = self.joining_tables(barley_2078, maize_2078, buckwheat_2078, millet_2078, wheat_2078, paddy_2078, s_paddy_2078, m_paddy_2078)

        final_2078.replace('-', 0, inplace=True)
        final_2078['Millet_yield'] = final_2078['Millet_yield'].astype(float)
        final_2078['Paddy_total_yield'] = final_2078['Paddy_total_yield'].astype(float)
        final_2078['Paddy_spring_yield'] = final_2078['Paddy_spring_yield'].astype(float)
        final_2078['Paddy_main_yield'] = final_2078['Paddy_main_yield'].astype(float)
        final_2078['Barley_yield'] = final_2078['Barley_yield'].astype(float)
        final_2078['Buckwheat_yield'] = final_2078['Buckwheat_yield'].astype(float)
        return final_2078       



    def data_2077(self):
      
        barley_2077 = self.json_to_df('raw_datas/2077_data/barley_yield2077.json',  2077)
        maize_2077 = self.json_to_df('raw_datas/2077_data/maize_yield2077.json', 2077)
        buckwheat_2077 = self.json_to_df('raw_datas/2077_data/buckwheat_yield2077.json',  2077)
        millet_2077 = self.json_to_df('raw_datas/2077_data/millet_yield2077.json',  2077)
        wheat_2077 =  self.json_to_df('raw_datas/2077_data/wheat_yield2077.json',  2077)
        paddy_2077 =  self.paddy_json_to_df('raw_datas/2077_data/2077_paddy_yield.json',  2077)
        s_paddy_2077 = self.Spaddy_json_to_df('raw_datas/2077_data/2077_paddy_yield.json',  2077)
        m_paddy_2077 = self.Mpaddy_json_to_df('raw_datas/2077_data/2077_paddy_yield.json',  2077)
        
        final_2077 = self.joining_tables(barley_2077, maize_2077, buckwheat_2077, millet_2077, wheat_2077, paddy_2077, s_paddy_2077, m_paddy_2077)

        final_2077.replace('-', 0, inplace=True)
        final_2077['Millet_yield'] = final_2077['Millet_yield'].astype(float)
        final_2077['Paddy_total_yield'] = final_2077['Paddy_total_yield'].astype(float)
        final_2077['Paddy_spring_yield'] = final_2077['Paddy_spring_yield'].astype(float)
        final_2077['Paddy_main_yield'] = final_2077['Paddy_main_yield'].astype(float)
        final_2077['Barley_yield'] = final_2077['Barley_yield'].astype(float)
        final_2077['Buckwheat_yield'] = final_2077['Buckwheat_yield'].astype(float)
        return final_2077       


    def data_2076(self):
      
        barley_2076 = self.json_to_df('raw_datas/2076_data/barley_yield2076.json',  2076)
        maize_2076 = self.json_to_df('raw_datas/2076_data/maize_yield2076.json', 2076)
        buckwheat_2076 = self.json_to_df('raw_datas/2076_data/buckwheat_yield2076.json',  2076)
        millet_2076 = self.json_to_df('raw_datas/2076_data/millet_yield2076.json',  2076)
        wheat_2076 =  self.json_to_df('raw_datas/2076_data/wheat_yield2076.json',  2076)
        paddy_2076 =  self.paddy_json_to_df('raw_datas/2076_data/2076_paddy_yield.json',  2076)
        s_paddy_2076 = self.Spaddy_json_to_df('raw_datas/2076_data/2076_paddy_yield.json',   2076)
        m_paddy_2076 = self.Mpaddy_json_to_df('raw_datas/2076_data/2076_paddy_yield.json',  2076)
     
        final_2076 = self.joining_tables(barley_2076, maize_2076, buckwheat_2076, millet_2076, wheat_2076, paddy_2076, s_paddy_2076, m_paddy_2076)

        final_2076.replace('-', 0, inplace=True)
        final_2076['Millet_yield'] = final_2076['Millet_yield'].astype(float)
        final_2076['Paddy_total_yield'] = final_2076['Paddy_total_yield'].astype(float)
        final_2076['Paddy_spring_yield'] = final_2076['Paddy_spring_yield'].astype(float)
        final_2076['Paddy_main_yield'] = final_2076['Paddy_main_yield'].astype(float)
        final_2076['Barley_yield'] = final_2076['Barley_yield'].astype(float)
        final_2076['Buckwheat_yield'] = final_2076['Buckwheat_yield'].astype(float)
        return final_2076       


    def total_yield_data(self):
        data_2076 = self.data_2076()
        data_2077 = self.data_2077()
        data_2079 = self.final_2079_data()
        data_2078 = self.data_2078()
        
        df = pd.concat([data_2078,data_2076, data_2077, data_2079])
        df.to_csv('full_data.csv', index = False)

    def merging_potato(self):
        potato = self.json_to_df('raw_datas/potato_yield2076.json', 2076)
        potato77 = self.json_to_df('raw_datas/potato_yield2077.json', 2077)
        potato78 = pd.read_csv('raw_datas/2078_data/potato78.csv')
        potato79 = pd.read_csv('raw_datas/2079_data/potato79.csv')
        rest = pd.read_csv('raw_datas/full_data.csv')
        potato_years = pd.concat([potato, potato77, potato78, potato79])
        potato_years.to_csv('trial_potato.csv', index= False)
        potato_merge = self.joining_tables1(rest,  potato_years)
        print(potato_merge) 
        potato_merge.replace('-', 0, inplace=True)
        potato_merge.to_csv('potato_wala.csv', index = False)

    def merging_coffee(self):
        coffee76 = pd.read_csv('raw_datas/2076_data/coffee76.csv')
        coffee77 = self.json_to_df('raw_datas/2077_data/coffee_yield2077.json', 2077)
        coffee78 = pd.read_csv('raw_datas/2078_data/coffee78.csv')
        coffee79 = self.json_to_df('raw_datas/2079_data/coffee_yield2079.json', 2079)
    
        rest = pd.read_csv('raw_datas/full_data_with_potato.csv')
        coffee_years = pd.concat([coffee76, coffee77, coffee78, coffee79])
        coffee_years.to_csv('trial_coffee.csv', index= False)
        potato_merge = self.joining_tables1(rest,  coffee_years)
        print(potato_merge)     
        potato_merge.replace('-', 0, inplace=True)
        potato_merge.to_csv('coffee_wala.csv', index = False)

    def merging_tea(self):
        tea = pd.read_csv('raw_datas/tea.csv')
        rest = pd.read_csv('raw_datas/full_data_with_coffee_wala.csv')
        tea_merge = self.joining_tables1(rest,  tea)
        print(tea_merge)     
        tea_merge.replace('-', 0, inplace=True)
        tea_merge.to_csv('tea_wala.csv', index = False)

    def merging_lentil(self):
        lentil76 = self.json_to_df('raw_datas/2076_data/pulse_yield2076.json', 2076)
        lentil77 = self.json_to_df('raw_datas/2077_data/lentil2077.json', 2077)
        lentil78 = self.json_to_df('raw_datas/2078_data/pulse_yield2078.json', 2078)
        lentil79 = self.json_to_df('raw_datas/2079_data/lentil2079.json', 2079)
        rest = pd.read_csv('raw_datas/final_data_tea_samma.csv')
        lentil_years = pd.concat([lentil76, lentil77, lentil78, lentil79])
        lentil_years.to_csv('trial_lentil.csv', index= False)
        lentil_merge = self.joining_tables1(rest,  lentil_years)
        print(lentil_merge)     
        lentil_merge.replace('-', 0, inplace=True)
        lentil_merge.to_csv('lentil_wala.csv', index = False)


    def merging_jute(self):
        jute = pd.read_csv('raw_datas/jute.csv')
        rest = pd.read_csv('raw_datas/final_lentil_samma.csv')
        jute_merge = self.joining_tables1(rest,  jute)
        print(jute_merge)     
        jute_merge.replace('-', 0, inplace=True)
        jute_merge.to_csv('jute_samma.csv', index = False)



    def merging_cotton(self):
        jute = pd.read_csv('raw_datas/cotton.csv')
        rest = pd.read_csv('raw_datas/jute_samma.csv')
        jute_merge = self.joining_tables1(rest,  jute)
        print(jute_merge)     
        jute_merge.replace('-', 0, inplace=True)
        jute_merge.to_csv('final_bhayo.csv', index = False)


if __name__ == "__main__":
    a = ABC()
    # a.Spaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
    # a.Mpaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
    a.merging_cotton()
        

