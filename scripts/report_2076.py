from repo.pdf_to_data import FormatConverter
import json


fc = FormatConverter


def wheat_maize_yield():
    wheat_maize_data = fc.converting_csv_to_table_data("./data/maize76.csv")
    filtered = fc.filtering_needed_data(extracted_data = wheat_maize_data, 
                                        starting_chr=['1',	'TAPLEJUNG',	'9,968',	'34,160',	'3.43',	'1,538',	'2,876',	'1.87'], 
                                        ending_chr=['SUDURPASHCHIM',	'KANCHANPUR',	'3,168',	'7,404',	'2.34',	'33,073',	'84,544',	'2.56'], 
                                        total_columns=8)
    headings = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield']
    grouping = fc.groups_to_json(groups=filtered,  heading = headings)
    maize_data = [{'District': entry['District'],
                    'Maize_yield': entry['MaizeYield']
                    } for entry in grouping]

    wheat_data = [{'District': entry['District'],
                   'Wheat_yield': entry['WheatYield']
                   } for entry in grouping]
    print(wheat_data)
    print(maize_data)
    file_path1 = './data/maize_yield2076.json'
    file_path2 = './data/wheat_yield2076.json'

    with open(file_path1, 'w') as json_file:
        json.dump(maize_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(wheat_data, json_file)
    return wheat_data, maize_data

def millet_barley():
    millet_barley_data = fc.converting_csv_to_table_data("./data/millet76.csv")
    filtered = fc.filtering_needed_data(extracted_data = millet_barley_data, 
                                        starting_chr=['1',	'TAPLEJUNG',	'3005',	'4193',	'1.4',	'265',	'364',	'1.37',	'109',	'153',	'1.4'], 
                                        ending_chr=['SUDURPASHCHIM',	'KANCHANPUR',	'0',	'0',	'0',	'8',	'10',	'1.25',	'0',	'0',	'-'], 
                                        total_columns=11)
    headings = ['Province', 'District', 'MArea', 'MProduction', 'MYield', 'BArea', 'BProduction', 'BYield', 'BarArea', 'BarProduction', 'BarYield']
    grouping = fc.groups_to_json(groups=filtered,  heading = headings)    
    millet_data = [{'District': entry['District'],
                    'Millet_yield': entry['MYield']
                    } for entry in grouping]

    barley_data = [{'District': entry['District'],
                   'Barley_yield': entry['BYield']
                   } for entry in grouping]
    
    buckwheat_data = [{'District': entry['District'],
                   'Buckwheat_yield': entry['BarYield']
                   } for entry in grouping]
    print(millet_data)
    print(buckwheat_data)
    print(barley_data)
    file_path1 = './data/millet_yield2076.json'
    file_path2 = './data/buckwheat_yield2076.json'
    file_path3 = './data/barley_yield2076.json'

    with open(file_path1, 'w') as json_file:
        json.dump(millet_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(buckwheat_data, json_file)
    with open(file_path3, 'w') as json_file:
        json.dump(barley_data, json_file)
    return millet_data, buckwheat_data, barley_data



def paddy_yield():
    paddy_data = fc.converting_csv_to_table_data("./data/paddy76.csv")
    filtered = fc.filtering_needed_data(extracted_data = paddy_data, 
                                        starting_chr=['1',	'TAPLEJUNG',	'-',	'-',	'-',	'3877',	'10352',	'2.67',	'3877',	'10352',	'2.67'], 
                                        ending_chr=['SUDURPASHCHIM','KANCHANPUR',	'700',	'3133',	'4.48',	'45515',	'176182',	'3.87',	'46215',	'179314',	'3.88'], 
                                        total_columns=11)
    headings =  ['Province', 'District', 'SArea', 'SProduction', 'SpringYield', 'MArea', 'MProduction', 'MainYield', 'TArea', 'TProduction', 'TotalYield']
    grouping = fc.groups_to_json(groups=filtered,  heading = headings)
    paddy_data = [{'District': entry['District'],
                    'Spring_yield': entry['SpringYield'],
                    'Main_yield': entry['MainYield'],
                    'Total_yield': entry['TotalYield'],
                    } for entry in grouping]


    print(paddy_data)
    file_path1 = './data/2077_paddy_yield.json'
  

    with open(file_path1, 'w') as json_file:
        json.dump(paddy_data, json_file)

    return paddy_data


if __name__ == '__main__':
    paddy_yield()
    # millet_barley()
    # wheat_maize_yield()