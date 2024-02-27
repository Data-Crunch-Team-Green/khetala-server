import json 


class YieldData:
    def __init__(self):
        with open("raw_datas/2079_data/barley_yield.json") as p1:
            self.barley_2079 = json.load(p1)
        with open("raw_datas/2079_data/buckwheat_yield.json") as p2:
            self.buckwheat_2079 = json.load(p2)
        with open("raw_datas/2079_data/maize_yield.json") as p3:
            self.maize_2079 = json.load(p3)
        with open("raw_datas/2079_data/millet_yield.json") as p4:
            self.millet_2079 = json.load(p4)
        with open("raw_datas/2079_data/paddy_yield.json") as p5:
            self.paddy_2079 = json.load(p5)
        with open("raw_datas/2079_data/wheat_yield.json") as p6:
            self.wheat_2079 = json.load(p6)
        with open("raw_datas/2076_data/2076_paddy_yield.json") as p7:
            self.paddy_2076 = json.load(p7)
        with open("raw_datas/2077_data/2077_paddy_yield.json") as p8:
            self.paddy_2077 = json.load(p8)
        with open("raw_datas/2078_data/2078_paddy_yield.json") as p9:
            self.paddy_2078 = json.load(p9)
        with open("raw_datas/2078_data/maize_yield2078.json") as p10:
            self.maize_2078 = json.load(p10)
        with open("raw_datas/2078_data/barley_yield.json") as p11:
            self.barley_2078 = json.load(p11)
        with open("raw_datas/2078_data/buckwheat_yield.json") as p12:
            self.buckwheat_2078 = json.load(p12)
        with open("raw_datas/2078_data/millet_yield.json") as p13:
            self.millet_2078 = json.load(p13)
        with open("raw_datas/2078_data/wheat_yield2078.json") as p14:
            self.wheat_2078 = json.load(p14)


    def district_wise_data(self, district, data_pool):
        district_yield_data = []

        for pair in data_pool:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Barley_yield':
                        district_yield_data.append({key: value})

    def lates_percent_change_in_yield_district_wise(self, district, crop):
        crop_name = crop.upper()
        if crop_name == 'MAIZE':
            latest_year_data = self.maize_2079
            prev_year_data = self.maize_2078
            key_heading = 'Maize_yield'
        elif crop_name == 'BARLEY':
            latest_year_data = self.barley_2079
            prev_year_data = self.barley_2078
            key_heading = 'Barley_yield'
        elif crop_name == 'MILLET':
            latest_year_data = self.millet_2079
            prev_year_data = self.millet_2078
            key_heading = 'Millet_yield'
            key_heading = '_yield'
        elif crop_name == 'BUCKWHEAT':
            latest_year_data = self.buckwheat_2079
            prev_year_data = self.buckwheat_2078
            key_heading = 'Buckwheat_yield'
        elif crop_name == 'WHEAT':
            latest_year_data = self.wheat_2079
            prev_year_data = self.wheat_2078
            key_heading = 'Wheat_yield'
        
        
            
            
        
        district_data_latest = self.district_wise_data(district, latest_year_data)
        district_data_previous = self.district_wise_data(district, prev_year_data)

        latest_yield = 0
        prev_yield = 0
        for key, value in district_data_latest.items():
            if key == key_heading:
                latest_yield += value
        for key, value in district_data_previous.items():
            if key == key_heading:
                prev_yield += value 

        percent_change = ((latest_yield - prev_yield)/prev_yield ) * 100





    def district_wise_latest_year_yield(self, district):
        
        district_yield_data = []

        for pair in self.barley_2079:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Barley_yield':
                        district_yield_data.append({key: value})
        for pair in self.buckwheat_2079:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Buckwheat_yield':
                        district_yield_data.append({key: value})
        for pair in self.maize_2079:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Maize_yield':
                        district_yield_data.append({key: value})
        for pair in self.millet_2079:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Millet_yield':
                        district_yield_data.append({key: value})
        for pair in self.paddy_2079:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Total_yield':
                        district_yield_data.append({'Paddy_yield': value})
        for pair in self.wheat_2079:
            if pair['District'] == district:
                for key, value in pair.items():
                    if key == 'Wheat_yield':
                        district_yield_data.append({key: value})
        
        print(district_yield_data)
        return district_yield_data
    



    def barley_national_rank(self, district):
        data_2079 = self.barley_2079
        rank = 0
        simplified_data = []

        for a in data_2079:
            rank += 1
            if len(simplified_data)<1:
                k = a['District'] 
                v = a['Barley_yield']
                position = rank
                simplified_data.append({k:position})
            else:
                k = a['District'] 
                v = a['Barley_yield']
                position = rank
                simplified_data.append({k:position})                

        
        

        for a in range(len(simplified_data)):
            for b in simplified_data:
                pass


        


                    

