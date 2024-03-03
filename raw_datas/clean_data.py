
import pandas as pd 

class ABC:
    def json_to_df(self,path:str,  year:int):
        df = pd.read_json(path)
        df['Year'] = year
        reordered = df.iloc[:, [2,0,1]]
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




if __name__ == "__main__":
    a = ABC()
    # a.Spaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
    # a.Mpaddy_json_to_df('raw_datas/2078_data/2078_paddy_yield.json',  2078)
    a.total_yield_data()
        

