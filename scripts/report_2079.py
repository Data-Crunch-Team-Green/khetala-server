from repo.pdf_to_data import FormatConverter
import json


pdc = FormatConverter


def wheat_maize_yield():

    real_pg_no1 = pdc.page_number_converter(18)
    real_pg_no2 = pdc.page_number_converter(19)
    real_pg_no3 = pdc.page_number_converter(20)

    t1 = pdc.converting_pdf_to_table_data(real_pg_no1)
    t2 = pdc.converting_pdf_to_table_data(real_pg_no2)
    t3 = pdc.converting_pdf_to_table_data(real_pg_no3)
  

    table1 = pdc.converting_pdf_to_table_data(t1, 
    ['KOSHI', 'TAPLEJUNG','11,198','38,312', '3.42', '1,537', '2,875', '1.87'],
    ['KOSHI', 'SUNSARI', '9,034', '29,432', '3.26', '12,127', '41,195', '3.40'],
    8)  
    table2 = pdc.converting_pdf_to_table_data(t1, 
    ['MADHESH', 'SAPTARI','6,589', '23,211', '3.52', '15,017', '54,351', '3.62'],
    ['MADHESH', 'PARSA', '4,189', '17,166', '4.10', '23,008', '86,163', '3.74'],
    8)
    table3 = pdc.converting_pdf_to_table_data(t1, 
    ['BAGMATI', 'DOLAKHA','6,171', '22,155', '3.59', '4,246', '7,515', '1.77'],
    ['BAGMATI', 'BHAKTAPUR', '1,900', '7,750', '4.08', '3,150', '12,409', '3.94'],
    8)
    table4 = pdc.converting_pdf_to_table_data(t2, 
    ['BAGMATI', 'LALITPUR','8,573', '33,656', '3.93', '3,485', '11,858', '3.40'],
    ['BAGMATI', 'CHITWAN', '28,055', '105,239', '3.75', '5,151', '23,248', '4.51'],
    8)
    table5 = pdc.converting_pdf_to_table_data(t2, 
    ['GANDAKI', 'MANANG','177', '351', '1.98', '213', '500', '2.35'],
    ['GANDAKI', 'NAWALPARASI EAST', '5,101', '15,556', '3.05', '7,605', '20,930', '2.75'],
    8)
    table6 = pdc.converting_pdf_to_table_data(t3, 
    ['KARNALI', 'DOLPA','2,204','2,798', '1.27', '2,805', '4,010', '1.43'],
    ['KARNALI', 'SURKHET', '13,252', '46,756', '3.53', '12,191', '42,354', '3.47'],
    8)  
    table7 = pdc.converting_pdf_to_table_data(t3, 
    ['SUDURPASHCHIM', 'BAJURA', '3,293','4,850', '1.47', '10,450', '15,675', '1.50'],
    ['SUDURPASHCHIM', 'KANCHANPUR', '3,250', '11,534', '3.55', '31,355', '101,995', '3.25'],
    8)  
    table8 = pdc.converting_pdf_to_table_data(t2, 
    ['LUMBINI', 'PALPA', '21,643','55,779', '2.58', '5,786', '13,572', '2.35'],
    ['LUMBINI', 'ARGHAKHANCHI', '16,955', '54,975', '3.24', '7,340', '19,955', '2.72'],
    8) 
    table9 = pdc.converting_pdf_to_table_data(t2, 
    ['LUMBINI', 'RUPANDEHI', '2,751','10,752', '3.91', '26,118', '103,167', '3.95'],
    ['LUMBINI', 'ROLPA', '12,335', '38,500', '3.12', '8,596', '24,400', '2.84'],
    8) 

    added1 = pdc.groups_to_json(groups=table1,  
    heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added2 = pdc.groups_to_json(groups=table2,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added3 = pdc.groups_to_json(groups=table3,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added4 = pdc.groups_to_json(groups=table4,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added5 = pdc.groups_to_json(groups=table5,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added6 = pdc.groups_to_json(groups=table6,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added7 = pdc.groups_to_json(groups=table7,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added8 = pdc.groups_to_json(groups=table8,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added9 = pdc.groups_to_json(groups=table9,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])

   
    data = added1+added2+added3+added4+added5+added6+added7+added8+added9
    maize_data = [{'District': entry['District'],
                    'Maize_yield': entry['MaizeYield']
                    } for entry in data]

    wheat_data = [{'District': entry['District'],
                   'Wheat_yield': entry['WheatYield']
                   } for entry in data]
    print(wheat_data)
    print(maize_data)
    file_path1 = './data/maize_yield.json'
    file_path2 = './data/wheat_yield.json'

    with open(file_path1, 'w') as json_file:
        json.dump(maize_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(wheat_data, json_file)
    return wheat_data, maize_data




def paddy_yield():

    real_pg_no1 = pdc.page_number_converter(14)
    real_pg_no2 = pdc.page_number_converter(15)
    real_pg_no3 = pdc.page_number_converter(16)
    real_pg_no4 = pdc.page_number_converter(17)

    t1 = pdc.converting_pdf_to_table_data(real_pg_no1)
    t2 = pdc.converting_pdf_to_table_data(real_pg_no2)
    t3 = pdc.converting_pdf_to_table_data(real_pg_no3)
    t4 = pdc.converting_pdf_to_table_data(real_pg_no4)

    table1 = pdc.converting_pdf_to_table_data(t1, 
    ['KOSHI', 'TAPLEJUNG','35','145', '4.14', '6,737', '20,306', '3.01', '6,772', '20,451', '3.02'],
    ['KOSHI', 'SUNSARI', '5,260', '26,277', '5.00', '48,132', '174,043', '3.62', '53,392', '200,320', '3.75'],
    11)  
    table2 = pdc.converting_pdf_to_table_data(t1, 
    ['MADHESH', 'SAPTARI','550', '2,475', '4.50', '50,314', '169,720', '3.37', '50,864', '172,195', '3.39'],
    ['MADHESH','RAUTAHAT', '1,000','4,720', '4.72','39,529', '125,045','3.16','40,529', '129,765','3.20'],
    11)
    table3 = pdc.converting_pdf_to_table_data(t2, 
    ['MADHESH', 'BARA','15,105',	'66,613','4.41',	'40,093','147,940','3.69','55,198','214,553','3.89'],
    ['MADHESH','PARSA', '3,550','18,815','5.30','41,666','202,596','4.80','45,216','221,411', '4.90'],
    11)

    table4 = pdc.converting_pdf_to_table_data(t2, 
    ['BAGMATI',	'SINDHUPALCHOK',	'2,985',	'13,134',	'4.40',	'8,877',	'25,744',	'2.90',	'11,862',	'38,878',	'3.28'],
    ['BAGMATI',	'CHITWAN',	'4,975',	'20,980',	'4.22',	'22,428',	'83,564',	'3.73',	'27,403',	'104,544',	'3.82'],
    11)
    table5 = pdc.converting_pdf_to_table_data(t2, 
    ['GANDAKI',	'GORKHA',	'1,320',	'5,075',	'3.84',	'11,266',	'43,175',	'3.40',	'12,586',	'48,250',	'3.83'],
    ['GANDAKI',	'TANAHU',	'2,490',	'11,163',	'4.48',	'8,517',	'32,799',	'3.77',	'11,007',	'43,962',	'3.99'],
    11)
    table6 = pdc.converting_pdf_to_table_data(t3, 
    ['GANDAKI',	'KASKI',	'450',	'2,112',	'4.69',	'19,605',	'57,419',	'3.80',	'20,055',	'59,531',	'2.97'],
    ['GANDAKI',	'NAWALPARASI EAST',	'700',	'3,360',	'4.80',	'18,816',	'75,827',	'4.01',	'19,516',	'79,187',	'4.06'],
    11)  
    table7 = pdc.converting_pdf_to_table_data(t3, 
    ['LUMBINI',	'PALPA',	'770',	'3,002',	'3.90',	'7,005',	'26,619',	'3.80',	'7,775',	'29,621',	'3.81'],
    ['LUMBINI',	'ROLPA',	'-',	'-',	'-',	'4,407',	'11,617',	'2.64',	'4,407',	'11,617',	'2.64'],
    11)  
    table8 = pdc.converting_pdf_to_table_data(t4, 
    ['KARNALI',	'DOLPA',	'-',	'-',	'-',	'198',	'348',	'1.99',	'198',	'348',	'1.76'],
    ['KARNALI',	'SURKHET',	'139',	'624',	'4.49',	'12,679',	'50,279',	'4.18',	'12,818',	'50,903',	'3.97'],
    11) 
    table9 = pdc.converting_pdf_to_table_data(t4, 
    ['SUDURPASHCHIM',	'BAJURA',	'-',	'-',	'-',	'4,150',	'10,832',	'2.65',	'4,150',	'10,832',	'2.61'],
    ['SUDURPASHCHIM',	'KANCHANPUR',	'230',	'989',	'4.30',	'48,515',	'131,476',	'3.84',	'48,745',	'132,465',	'2.72'],
    11) 


    paddy_heading = ['Province', 'District', 'SArea', 'SProduction', 'SpringYield', 'MArea', 'MProduction', 'MainYield', 'TArea', 'TProduction', 'TotalYield']
    added1 = pdc.groups_to_json(groups=table1,  
    heading = paddy_heading )
    added2 = pdc.groups_to_json(groups=table2,  
        heading = paddy_heading)
    added3 = pdc.groups_to_json(groups=table3,  
        heading =paddy_heading)
    added4 = pdc.groups_to_json(groups=table4,  
        heading = paddy_heading)
    added5 = pdc.groups_to_json(groups=table5,  
        heading = paddy_heading)
    added6 = pdc.groups_to_json(groups=table6,  
        heading = paddy_heading)
    added7 = pdc.groups_to_json(groups=table7,  
        heading = paddy_heading)
    added8 = pdc.groups_to_json(groups=table8,  
        heading = paddy_heading)
    added9 = pdc.groups_to_json(groups=table9,  
        heading = paddy_heading)

   
    data = added1+added2+added3+added4+added5+added6+added7+added8+added9
    paddy_data = [{'District': entry['District'],
                    'Spring_yield': entry['SpringYield'],
                    'Main_yield': entry['MainYield'],
                    'Total_yield': entry['TotalYield'],
                    } for entry in data]


    print(paddy_data)
    file_path1 = './data/paddy_yield.json'
  

    with open(file_path1, 'w') as json_file:
        json.dump(paddy_data, json_file)

    return paddy_data



def millet_barley_yield():

    real_pg_no1 = pdc.page_number_converter(21)
    real_pg_no2 = pdc.page_number_converter(22)
    real_pg_no3 = pdc.page_number_converter(23)
    real_pg_no4 = pdc.page_number_converter(24)


    t1 = pdc.converting_pdf_to_table_data(real_pg_no1)
    t2 = pdc.converting_pdf_to_table_data(real_pg_no2)
    t3 = pdc.converting_pdf_to_table_data(real_pg_no3)
    t4 = pdc.converting_pdf_to_table_data(real_pg_no4)

    table1 = pdc.converting_pdf_to_table_data(t1, 
    ['KOSHI',	'TAPLEJUNG',	'2,987',	'4,242',	'1.42',	'131',	'174',	'1.32',	'269',	'405',	'1.51'],
    ['KOSHI',	'SUNSARI',	'505',	'585',	'1.16',	'299',	'380',	'1.27',	'14',	'22',	'1.57'],
    11)  
    table2 = pdc.converting_pdf_to_table_data(t1, 
    ['MADHESH',	'SAPTARI',	'183',	'231',	'1.26',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['MADHESH',	'PARSA',	'-',	'-',	'-',	'-',	'-',	'-',	'29',	'42',	'1.46'],
    11)
    table3 = pdc.converting_pdf_to_table_data(t2, 
    ['BAGMATI',	'DOLAKHA',	'3,659',	'4,854',	'1.33',	'1,057',	'1,160',	'1.10',	'136',	'165',	'1.21'],
    ['BAGMATI',	'CHITWAN',	'1,478',	'1,693',	'1.15',	'1,300',	'1,393',	'1.07',	'15',	'28',	'1.87'],
    11)

    table4 = pdc.converting_pdf_to_table_data(t4, 
    ['SUDURPASHCHIM',	'BAJURA',	'5,870',	'5,907',	'1.01',	'255',	'267',	'1.05',	'1,470',	'1,970',	'1.34'],
    ['SUDURPASHCHIM',	'KANCHANPUR',	'-',	'-',	'-',	'-',	'-',	'-',	'133',	'232',	'1.74'],
    11) 
    table5 = pdc.converting_pdf_to_table_data(t2, 
    ['GANDAKI',	'MANANG',	'-',	'-',	'-',	'361',	'610',	'1.88',	'111',	'175',	'1.58'],
    ['GANDAKI',	'SYANGJA',	'16,501',	'20,346',	'1.23',	'273',	'294',	'1.08',	'6',	'6',	'1.00'],
    11)
    table6 = pdc.converting_pdf_to_table_data(t3, 
    ['GANDAKI',	'NAWALPARASI EAST',	'259',	'292',	'1.13',	'99',	'98',	'0.99',	'205',	'223',	'1.09'],
    ['GANDAKI','BAGLUNG',	'18,456',	'23,247',	'1.26',	'98',	'140',	'1.43',	'90',	'120',	'1.33'],
    11)  
    table7 = pdc.converting_pdf_to_table_data(t3, 
    ['LUMBINI',	'PALPA',	'2,684',	'3,762',	'1.40',	'438',	'403',	'0.92',	'24.0',	'24.2',	'1.01'],
    ['LUMBINI',	'NAWALPARASI WEST',	'228',	'238',	'1.04',	'6',	'7',	'1.28',	'5',	'6',	'1.23'],
    11)  
    table8 = pdc.converting_pdf_to_table_data(t3, 
    ['LUMBINI',	'RUKUM EAST',	'641',	'833',	'1.30',	'163',	'187',	'1.15',	'962',	'967',	'1.01',],
    ['LUMBINI',	'ROLPA',	'1,126',	'1,498',	'1.33',	'102',	'95',	'0.93',	'620',	'625',	'1.01'],
    11) 
    table9 = pdc.converting_pdf_to_table_data(t3, 
    ['KARNALI',	'DOLPA',	'280',	'310',	'1.11',	'986',	'858',	'0.87',	'334',	'345',	'1.03'],
    ['KARNALI',	'RUKUM WEST',	'466',	'633',	'1.36',	'165',	'206',	'1.25',	'480',	'702',	'1.46'],
    11) 

    table10 = pdc.converting_pdf_to_table_data(t3, 
    ['KARNALI',	'DOLPA',	'280',	'310',	'1.11',	'986',	'858',	'0.87',	'334',	'345',	'1.03'],
    ['KARNALI',	'RUKUM WEST',	'466',	'633',	'1.36',	'165',	'206',	'1.25',	'480',	'702',	'1.46'],
    11) 

    table11 = pdc.converting_pdf_to_table_data(t4, 
    ['KARNALI',	'SALYAN',	'1,231',	'1,314',	'1.07',	'74',	'89',	'1.19',	'749',	'1,275',	'1.70'],
    ['KARNALI',	'SURKHET',	'2,995',	'3,497',	'1.17',	'56',	'85',	'1.52',	'630',	'1,105',	'1.75'],
    11) 



    paddy_heading = ['Province', 'District', 'MArea', 'MProduction', 'MYield', 'BArea', 'BProduction', 'BYield', 'BarArea', 'BarProduction', 'BarYield']
    added1 = pdc.groups_to_json(groups=table1,  
    heading = paddy_heading )
    added2 = pdc.groups_to_json(groups=table2,  
        heading = paddy_heading)
    added3 = pdc.groups_to_json(groups=table3,  
        heading =paddy_heading)
    added4 = pdc.groups_to_json(groups=table4,  
        heading = paddy_heading)
    added5 = pdc.groups_to_json(groups=table5,  
        heading = paddy_heading)
    added6 = pdc.groups_to_json(groups=table6,  
        heading = paddy_heading)
    added7 = pdc.groups_to_json(groups=table7,  
        heading = paddy_heading)
    added8 = pdc.groups_to_json(groups=table8,  
        heading = paddy_heading)
    added9 = pdc.groups_to_json(groups=table9,  
        heading = paddy_heading)
    added10 = pdc.groups_to_json(groups=table10,  
        heading = paddy_heading)
    added11 = pdc.groups_to_json(groups=table11,  
        heading = paddy_heading)
 
    data = added1+added2+added3+added4+added5+added6+added7+added8+added9+added10+added11

    file_path1 = './data/millet_yield.json'
    file_path2 = './data/buckwheat_yield.json'
    file_path3 = './data/barley_yield.json'
  
    millet_data = [{'District': entry['District'],
                    'Millet_yield': entry['MYield']
                    } for entry in data]

    buckwheat_data = [{'District': entry['District'],
                   'Buckwheat_yield': entry['BYield']
                   } for entry in data]
    
    barley_data = [{'District': entry['District'],
                   'Barley_yield': entry['BarYield']
                   } for entry in data]
    print(millet_data)
    print(buckwheat_data)
    print(barley_data)
    file_path1 = './data/millet_yield.json'
    file_path2 = './data/buckwheat_yield.json'
    file_path3 = './data/barley_yield.json'

    with open(file_path1, 'w') as json_file:
        json.dump(millet_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(buckwheat_data, json_file)
    with open(file_path3, 'w') as json_file:
        json.dump(barley_data, json_file)
    return millet_data, buckwheat_data, barley_data




def coffee_yield():

    t1 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 38+9)
    t2 = pdc.converting_pdf_to_table_data('./raw_datas/2079_data/report1.pdf', 39+9)

    table1 = pdc.filtering_needed_data(t1, 
    ['1',	'ARGHAKHANCHI',	'1,705',	'130',	'16',	'123.08'],
    ['16',	'KASKI',	'4,305',	'169',	'21',	'124.26'],
    6)  

    table2 = pdc.filtering_needed_data(t1, 
    ['18',	'KHOTANG',	'255',	'34',	'1.4',	'41.18'],
    ['29',	'PARBAT',	'1,840',	'127',	'12.5',	'98.43'],
    6)  

    table3 = pdc.filtering_needed_data(t2, 
    ['30',	'PYUTHAN',	'175',	'37',	'4.5',	'121.62'],
    ['44',	'UDAYAPUR',	'92',	'15',	'1.2',	'80.00'],
    6)  

   
    headings = ['sno', 'District', 'plant1', 'plant2','production', 'yield']

    
    added1 = pdc.groups_to_json(groups=table1,  
    heading = headings )
    added2 = pdc.groups_to_json(groups=table2,  
    heading = headings )
    added3 = pdc.groups_to_json(groups=table3,  
    heading = headings )




    data = added1+added2+added3
    coffee_data = [{'District': entry['District'],
                    'Coffee_yield': entry['yield']
                    } for entry in data]

    print(coffee_data)
    file_path1 = './raw_datas/coffee_yield2079.json'
 
    with open(file_path1, 'w') as json_file:
        json.dump(coffee_data, json_file)
   
    return coffee_data






if __name__ == '__main__':
    coffee_yield()
    # paddy_yield()
    # millet_barley_yield()



  