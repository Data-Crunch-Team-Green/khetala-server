from repo.pdf_to_data import FormatConverter
import json


fc = FormatConverter
pdc = FormatConverter

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
    paddy_data = fc.converting_csv_to_table_data("./raw_data/paddy76.csv")
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


def potato_yield():

    t1 = "./raw_datas/2076_data/potato.csv"  #path name
   
    table1 = pdc.converting_csv_to_table_data(t1)  
    filtered = pdc.filtering_needed_data(table1, 
    ['2',	'SAPTARI',	'6722',	'6718',	'1',	'201',	'8040',	'40',	'4178',	'63252',	'15.14'],
    ['SUDURPASHCHIM',	'KANCHANPUR',	'9906',	'11781',	'1.19',	'8042',	'397114',	'49.38',	'1694',	'27574',	'16.27'],
    11)
  


    headings = ['Province', 'District', 'OilArea', 'OilProduction', 'OilYield', 'sArea', 'sProduction', 'sYield', 'PArea', 'PProduction', 'PYield']

    added1 = pdc.groups_to_json(groups=filtered,  
    heading = headings)

   
    data = added1
    potato_data = [{'District': entry['District'],
                    'Potato_yield': entry['PYield']
                    } for entry in data]

    print(potato_data)
    file_path1 = './raw_datas/r_potato_yield2076.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(potato_data, json_file)
   
    return potato_data



def coffee_yield():

    # real_pg_no1 = pdc.page_number_converter(41)
   
   
    t1 = pdc.converting_pdf_to_table_data('./raw_datas/2078_data/report.pdf', 53)

    table1 = pdc.filtering_needed_data(t1, 
    ['1', 'ARGHAKHANCHI',	'1,705',	'130',	'16',	'123.08'],
    ['29',	'PARBAT',	'1,840',	'127',	'12.5',	'98.43'],
    6)  
  

    headings = ['Sn', 'District', 'pop', 'green', 'OilYield', 'Yield']

    # paddy_heading = ['Province', 'District', 'MArea', 'MProduction', 'MYield', 'BArea', 'BProduction', 'BYield', 'BarArea', 'BarProduction', 'BarYield']
    added1 = pdc.groups_to_json(groups=table1,  
    heading = headings )
   



    data = added1
    potato_data = [{'District': entry['District'],
                    'Coffee_yield': entry['Yield']
                    } for entry in data]

    print(potato_data)
    file_path1 = './raw_datas/coffee_yield2076.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(potato_data, json_file)
   
    return potato_data



def pulses_yield77():

    t1 = pdc.converting_pdf_to_table_data('./raw_datas/2077_data/report2077.pdf', 67-1)
    t2 = pdc.converting_pdf_to_table_data('./raw_datas/2077_data/report2077.pdf', 68-1)
    t3 = pdc.converting_pdf_to_table_data('./raw_datas/2077_data/report2077.pdf', 69-1)
    
    table1 = pdc.filtering_needed_data(t1, 
    ['1',	'TAPLEJUNG',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['1',	'SUNSARI',	'6,620',	'8,045',	'1.22',	'100',	'138',	'1.38',	'220',	'190',	'0.86'],
    11)  

    table2 = pdc.filtering_needed_data(t1, 
    ['2',	'SAPTARI',	'9,595',	'11,934',	'1.24',	'784',	'975',	'1.24',	'570',	'622',	'1.09'],
    ['2',	'PARSA',	'10,136',	'12,653',	'1.25',	'154',	'217',	'1.40',	'194',	'211',	'1.09'],
    11)  

    table3 = pdc.filtering_needed_data(t1, 
    ['Bagmati',	'DOLAKHA',	'20',	'12',	'0.60',	'7',	'5',	'0.71',	'2',	'2',	'1.00'],
    ['Bagmati',	'RAMECHAP',	'61',	'71',	'1.16',	'45',	'40',	'0.89',	'-',	'-',	'-'],
    11)  

    table4 = pdc.filtering_needed_data(t2, 
    ['Gandaki',	'MANANG',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['Gandaki',	'NAWALPARASIEAST',	'4,346',	'5,181',	'1.19',	'113',	'134',	'1.18',	'213',	'108',	'0.50'],
    11)  

    table5 = pdc.filtering_needed_data(t2, 
    ['Bagmati',	'SINDHULI',	'39',	'21',	'0.54',	'-',	'-',	'-',	'3',	'2',	'0.67'],
    ['Bagmati',	'CHITWAN',	'2,500',	'2,875',	'1.15',	'10',	'11',	'1.10',	'13',	'16',	'1.23'],
    11)  

    table6 = pdc.filtering_needed_data(t2, 
    ['Lumbini',	'PALPA',	'141',	'152',	'1.08',	'248',	'249',	'1.00',	'48',	'50',	'1.04'],
    ['Lumbini',	'KAPILBASTU',	'5,376',	'5,560',	'1.03',	'349',	'415',	'1.19',	'275',	'252',	'0.92'],
    11)  

    table7 = pdc.filtering_needed_data(t3, 
    ['Lumbini',	'DANG',	'27,600',	'33,872',	'1.23',	'375',	'338',	'0.90',	'310',	'387',	'1.25'],
    ['Lumbini',	'ROLPA',	'134',	'126',	'0.94',	'50',	'56',	'1.12',	'-',	'-',	'-'],
    11)  

    table8 = pdc.filtering_needed_data(t3, 
    ['Karnali',	'DOLPA',	'2',	'1',	'0.52',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['Karnali',	'SURKHET',	'2,072',	'2,436',	'1.18',	'664',	'768',	'1.16',	'50',	'70',	'1.40'],
    11)  

    table9 = pdc.filtering_needed_data(t3, 
    ['Sudurpashchim',	'BAJURA',	'74',	'34',	'0.46',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['Sudurpashchim',	'KANCHANPUR',	'5,237',	'7,204',	'1.38',	'857',	'1,040',	'1.21',	'-',	'-',	'-'],
    11)  
  

    headings = ['province', 'District', 'Larea', 'Lprod', 'Lyield', 'Carea', 'Cprod', 'Cyield', 'Parea', 'Pprod', 'Pyield']

    added1 = pdc.groups_to_json(groups=table1,  
    heading = headings )
    added2 = pdc.groups_to_json(groups=table2,  
    heading = headings )
    added3 = pdc.groups_to_json(groups=table3,  
    heading = headings )
    added4 = pdc.groups_to_json(groups=table4,  
    heading = headings )
    added5 = pdc.groups_to_json(groups=table5,  
    heading = headings )
    added6 = pdc.groups_to_json(groups=table6,  
    heading = headings )
    added7 = pdc.groups_to_json(groups=table7,  
    heading = headings )
    added8 = pdc.groups_to_json(groups=table8,  
    heading = headings )
    added9 = pdc.groups_to_json(groups=table9,  
    heading = headings )
   

    data = added1+added2+added3+added4+added5+added6+added7+added8+added9
    pulses_data = [{'District': entry['District'],
                    'Lentil_yield': entry['Lyield'],
                    'Chickenpea_yield': entry['Cyield'],
                    'Pigeon_yield': entry['Pyield'],
                    } for entry in data]

    print(pulses_data)
    file_path1 = './raw_datas/lentil2077.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(pulses_data, json_file)
   
    return pulses_data


def pulses_yield79():

    t1 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 52+9)
    t2 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 53+9)
    t3 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 54+9)
    t4 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 55+9)
    
    table1 = pdc.filtering_needed_data(t1, 
    ['KOSHI',	'TAPLEJUNG',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['KOSHI',	'SUNSARI',	'6,625',	'8,048',	'1.21',	'102',	'140',	'1.37',	'221',	'191',	'0.86',	'542',	'353',	'0.65'],
    14)  

    table2 = pdc.filtering_needed_data(t1, 
    ['MADHESH',	'SAPTARI',	'10,020',	'13,035',	'1.30',	'780',	'932',	'1.19',	'557',	'552',	'0.99',	'148',	'144',	'0.97'],
    ['MADHESH',	'PARSA',	'9,766',	'12,014',	'1.23',	'245',	'297',	'1.21',	'189',	'206',	'1.09',	'78',	'67',	'0.87'],
    14)  

    table3 = pdc.filtering_needed_data(t2, 
    ['BAGMATI',	'DOLAKHA',	'20',	'22',	'1.10',	'7',	'5',	'0.71',	'2',	'2',	'1.00',	'144',	'137',	'0.95'],
    ['BAGMATI',	'NUWAKOT',	'48',	'49',	'1.02',	'30',	'28',	'0.94',	'5',	'2',	'0.44',	'177',	'165',	'0.93'],
    14)  

    table4 = pdc.filtering_needed_data(t2, 
    ['GANDAKI',	'MANANG',	'-',	'-',	'-',	'2',	'1',	'0.63',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['GANDAKI',	'MYAGDI',	'20',	'20',	'1.01',	'-',	'-',	'-',	'29',	'41',	'1.39',	'155',	'157',	'1.01'],
    14)  

    table5 = pdc.filtering_needed_data(t3, 
    ['LUMBINI',	'PALPA',	'142',	'153',	'1.08',	'242',	'255',	'1.05',	'48',	'45',	'0.93',	'108',	'94',	'0.87'],
    ['LUMBINI',	'ROLPA',	'134',	'126',	'0.94',	'50',	'56',	'1.12',	'-',	'-',	'-',	'144',	'122',	'0.85'],
    14)  

    table6 = pdc.filtering_needed_data(t3, 
    ['KARNALI',	'DOLPA',	'1',	'0',	'0.26',	'-',	'-',	'-',	'-',	'-',	'-',	'2',	'2',	'1.06'],
    ['KARNALI',	'SALYAN',	'800',	'853',	'1.07',	'360',	'374',	'1.04',	'10',	'10',	'1.10',	'101',	'99',	'0.98'],
    14)  

    table7 = pdc.filtering_needed_data(t4, 
    ['KARNALI',	'JAJARKOT',	'599',	'466',	'0.78',	'29',	'34',	'1.18',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['KARNALI',	'SURKHET',	'1,105',	'1,023',	'0.93',	'555',	'592',	'1.07',	'25',	'18',	'0.70',	'227',	'258',	'1.14'],
    14)  

    table8 = pdc.filtering_needed_data(t4, 
    ['SUDURPASHCHIM',	'BAJURA',	'110',	'48',	'0.44',	'1',	'1',	'1.00',	'6',	'2',	'0.25',	'138',	'132',	'0.95'],
    ['SUDURPASHCHIM',	'KANCHANPUR',	'4,158',	'5,398',	'1.30',	'827',	'1,047',	'1.27',	'-',	'-',	'-',	'205',	'204',	'1.00',],
    14)  

    # table9 = pdc.filtering_needed_data(t3, 
    # ['Sudurpashchim',	'BAJURA',	'74',	'34',	'0.46',	'-',	'-',	'-',	'-',	'-',	'-'],
    # ['Sudurpashchim',	'KANCHANPUR',	'5,237',	'7,204',	'1.38',	'857',	'1,040',	'1.21',	'-',	'-',	'-'],
    # 11)  
  

    headings = ['province', 'District', 'Larea', 'Lprod', 'Lyield', 'Carea', 'Cprod', 'Cyield', 'Parea', 'Pprod', 'Pyield', 'Barea', 'Bprod', 'Byield']

    added1 = pdc.groups_to_json(groups=table1,  
    heading = headings )
    added2 = pdc.groups_to_json(groups=table2,  
    heading = headings )
    added3 = pdc.groups_to_json(groups=table3,  
    heading = headings )
    added4 = pdc.groups_to_json(groups=table4,  
    heading = headings )
    added5 = pdc.groups_to_json(groups=table5,  
    heading = headings )
    added6 = pdc.groups_to_json(groups=table6,  
    heading = headings )
    added7 = pdc.groups_to_json(groups=table7,  
    heading = headings )
    added8 = pdc.groups_to_json(groups=table8,  
    heading = headings )

   

    data = added1+added2+added3+added4+added5+added6+added7+added8
    pulses_data = [{'District': entry['District'],
                    'Lentil_yield': entry['Lyield'],
                    'Chickenpea_yield': entry['Cyield'],
                    'Pigeon_yield': entry['Pyield'],
                    } for entry in data]

    print(pulses_data)
    file_path1 = './raw_datas/lentil2079.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(pulses_data, json_file)
   
    return pulses_data



def pulses_yield78():

    t1 = pdc.converting_pdf_to_table_data('./raw_datas/2078_data/report.pdf', 70)
    t2 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 53+9)
    t3 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 54+9)
    t4 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 55+9)
    
    table1 = pdc.filtering_needed_data(t1, 
    ['KOSHI',	'TAPLEJUNG',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['KOSHI',	'SUNSARI',	'6,625',	'8,048',	'1.21',	'102',	'140',	'1.37',	'221',	'191',	'0.86',	'542',	'353',	'0.65'],
    14)  

    table2 = pdc.filtering_needed_data(t1, 
    ['MADHESH',	'SAPTARI',	'10,020',	'13,035',	'1.30',	'780',	'932',	'1.19',	'557',	'552',	'0.99',	'148',	'144',	'0.97'],
    ['MADHESH',	'PARSA',	'9,766',	'12,014',	'1.23',	'245',	'297',	'1.21',	'189',	'206',	'1.09',	'78',	'67',	'0.87'],
    14)  

    table3 = pdc.filtering_needed_data(t2, 
    ['BAGMATI',	'DOLAKHA',	'20',	'22',	'1.10',	'7',	'5',	'0.71',	'2',	'2',	'1.00',	'144',	'137',	'0.95'],
    ['BAGMATI',	'NUWAKOT',	'48',	'49',	'1.02',	'30',	'28',	'0.94',	'5',	'2',	'0.44',	'177',	'165',	'0.93'],
    14)  

    table4 = pdc.filtering_needed_data(t2, 
    ['GANDAKI',	'MANANG',	'-',	'-',	'-',	'2',	'1',	'0.63',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['GANDAKI',	'MYAGDI',	'20',	'20',	'1.01',	'-',	'-',	'-',	'29',	'41',	'1.39',	'155',	'157',	'1.01'],
    14)  

    table5 = pdc.filtering_needed_data(t3, 
    ['LUMBINI',	'PALPA',	'142',	'153',	'1.08',	'242',	'255',	'1.05',	'48',	'45',	'0.93',	'108',	'94',	'0.87'],
    ['LUMBINI',	'ROLPA',	'134',	'126',	'0.94',	'50',	'56',	'1.12',	'-',	'-',	'-',	'144',	'122',	'0.85'],
    14)  

    table6 = pdc.filtering_needed_data(t3, 
    ['KARNALI',	'DOLPA',	'1',	'0',	'0.26',	'-',	'-',	'-',	'-',	'-',	'-',	'2',	'2',	'1.06'],
    ['KARNALI',	'SALYAN',	'800',	'853',	'1.07',	'360',	'374',	'1.04',	'10',	'10',	'1.10',	'101',	'99',	'0.98'],
    14)  

    table7 = pdc.filtering_needed_data(t4, 
    ['KARNALI',	'JAJARKOT',	'599',	'466',	'0.78',	'29',	'34',	'1.18',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['KARNALI',	'SURKHET',	'1,105',	'1,023',	'0.93',	'555',	'592',	'1.07',	'25',	'18',	'0.70',	'227',	'258',	'1.14'],
    14)  

    table8 = pdc.filtering_needed_data(t4, 
    ['SUDURPASHCHIM',	'BAJURA',	'110',	'48',	'0.44',	'1',	'1',	'1.00',	'6',	'2',	'0.25',	'138',	'132',	'0.95'],
    ['SUDURPASHCHIM',	'KANCHANPUR',	'4,158',	'5,398',	'1.30',	'827',	'1,047',	'1.27',	'-',	'-',	'-',	'205',	'204',	'1.00',],
    14)  

    # table9 = pdc.filtering_needed_data(t3, 
    # ['Sudurpashchim',	'BAJURA',	'74',	'34',	'0.46',	'-',	'-',	'-',	'-',	'-',	'-'],
    # ['Sudurpashchim',	'KANCHANPUR',	'5,237',	'7,204',	'1.38',	'857',	'1,040',	'1.21',	'-',	'-',	'-'],
    # 11)  
  

    headings = ['province', 'District', 'Larea', 'Lprod', 'Lyield', 'Carea', 'Cprod', 'Cyield', 'Parea', 'Pprod', 'Pyield', 'Barea', 'Bprod', 'Byield']

    added1 = pdc.groups_to_json(groups=table1,  
    heading = headings )
    added2 = pdc.groups_to_json(groups=table2,  
    heading = headings )
    added3 = pdc.groups_to_json(groups=table3,  
    heading = headings )
    added4 = pdc.groups_to_json(groups=table4,  
    heading = headings )
    added5 = pdc.groups_to_json(groups=table5,  
    heading = headings )
    added6 = pdc.groups_to_json(groups=table6,  
    heading = headings )
    added7 = pdc.groups_to_json(groups=table7,  
    heading = headings )
    added8 = pdc.groups_to_json(groups=table8,  
    heading = headings )

   

    data = added1+added2+added3+added4+added5+added6+added7+added8
    pulses_data = [{'District': entry['District'],
                    'Lentil_yield': entry['Lyield'],
                    'Chickenpea_yield': entry['Cyield'],
                    'Pigeon_yield': entry['Pyield'],
                    } for entry in data]

    print(pulses_data)
    file_path1 = './raw_datas/lentil2079.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(pulses_data, json_file)
   
    return pulses_data




def pulses_yield76():

    t1 = "./raw_datas/pulse76.csv"  #path name
   
    table1 = pdc.converting_csv_to_table_data(t1)  
    filtered = pdc.filtering_needed_data(table1, 
    ['SANKHUWASABHA','1.27','0.92','-'],
    ['SURKHET','1.05','1.16','1.51'],
    4)
  
    headings = ['District', 'L_yield', 'C_yield', 'P_yield']

    added1 = pdc.groups_to_json(groups=filtered,  
    heading = headings)

   
    data = added1
    pulse_data = [{'District': entry['District'],
                    'Lentil_yield': entry['L_yield'],
                    'Chickpea_yield': entry['C_yield'],
                    'Pigeonpea_yield': entry['P_yield'],
                    } for entry in data]

    print(pulse_data)
    file_path1 = './raw_datas/2076_data/pulse_yield2076.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(pulse_data, json_file)
   
    return pulse_data



def pulses_yield78():

    t1 = "./raw_datas/pulse78.csv"  #path name
   
    table1 = pdc.converting_csv_to_table_data(t1)  
    filtered = pdc.filtering_needed_data(table1, 
    ['TAPLENJUNG','-','-','-'],
    ['KANCHANPUR','1.31','1.23','-'],
    4)
  
    headings = ['District', 'L_yield', 'C_yield', 'P_yield']

    added1 = pdc.groups_to_json(groups=filtered,  
    heading = headings)

   
    data = added1
    pulse_data = [{'District': entry['District'],
                    'Lentil_yield': entry['L_yield'],
                    'Chickpea_yield': entry['C_yield'],
                    'Pigeonpea_yield': entry['P_yield'],
                    } for entry in data]

    print(pulse_data)
    file_path1 = './raw_datas/2078_data/pulse_yield2078.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(pulse_data, json_file)
   
    return pulse_data



if __name__ == '__main__':
    pulses_yield78()
    # millet_barley()
    # wheat_maize_yield()