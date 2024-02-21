from repo.pdf_to_data import PdfConverter
import json


pdc = PdfConverter


def paddy_yield():

    real_pg_no1 = pdc.page_number_converter(17)
    real_pg_no2 = pdc.page_number_converter(18)
    real_pg_no3 = pdc.page_number_converter(19)
    real_pg_no4 = pdc.page_number_converter(20)


    table1 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1', 'TAPLEJUNG','32','135', '4.22', '7,405', '18,809', '2.54', '7,437', '18,944', '2.55'],
    ['1',	'SUNSARI',	'5,543',	'26,282',	'4.74',	'48,012',	'192,528',	'4.01',	'53,555',	'218,810',	'4.09'],
    11)  
    table2 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Madhesh',	'SAPTARI',	'875',	'3,981',	'4.55',	'49,450',	'174,064',	'3.52',	'50,325',	'178,045',	'3.54'],
    ['Madhesh',	'PARSA',	'3,550',	'16,259',	'4.58',	'39,463',	'159,825',	'4.05',	'43,013',	'176,084',	'4.09'],
    11)
    table3 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'SINDHUPALCHOK',	'3,200',	'14,240',	'4.45',	'8,782',	'22,043',	'2.51',	'11,982',	'36,283',	'3.03'],
    ['Bagmati',	'KAVRE',	'950',	'4,959',	'5.22',	'10,108',	'38,410',	'3.80',	'11,058',	'43,369',	'3.92'],
    11)

    table4 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'NUWAKOT',	'5,486',	'22,383',	'4.08',	'11,612',	'47,029',	'4.05',	'17,098',	'69,411',	'4.06'],
    ['Bagmati',	'CHITWAN',	'4,210',	'19,055',	'4.53',	'24,247',	'94,321',	'3.89',	'28,457',	'113,376',	'3.98'],
    11)
    table5 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'GORKHA',	'725',	'3,154',	'4.35',	'10,562',	'35,909',	'3.40',	'11,287',	'39,063',	'3.46'],
    ['Gandaki',	'SYANGJA',	'775',	'3,557',	'4.59',	'15,218',	'61,634',	'4.05',	'15,993',	'65,191',	'4.08'],
    11)
    # table6 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    # ['GANDAKI',	'KASKI',	'450',	'2,112',	'4.69',	'19,605',	'57,419',	'3.80',	'20,055',	'59,531',	'2.97'],
    # ['GANDAKI',	'NAWALPARASI EAST',	'700',	'3,360',	'4.80',	'18,816',	'75,827',	'4.01',	'19,516',	'79,187',	'4.06'],
    # 11)  
    table7 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Lumbini',	'PALPA',	'705',	'3,208',	'4.55',	'7,145',	'24,650',	'3.45',	'7,850',	'27,858',	'3.55'],
    ['Lumbini',	'ARGHAKHANCHI',	'400',	'1,768',	'4.42',	'5,985',	'19,451',	'3.25',	'6,385',	'21,219',	'3.32'],
    11)  
    # table8 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    # ['Lumbini',	'RUPANDEHI',	'345',	'1,842',	'5.34',	'63,813',	'269,929',	'4.23',	'64,158',	'271,771',	'4.24'],
    # ['Lumbini',	'BARDIYA',	'1,000',	'5,680',	'5.68',	'49,638',	'230,814',	'4.65',	'50,638',	'236,494',	'4.67'],
    # 11) 
    table9 = pdc.converting_pdf_to_table_data(real_pg_no4, 
    ['Sudurpashchim',	'DADELDHURA',	'44',	'199',	'4.52',	'5,917',	'20,414',	'3.45',	'5,961',	'20,613',	'3.46'],
    ['Sudurpashchim',	'KANCHANPUR',	'60',	'308',	'5.14',	'48,689',	'186,966',	'3.84',	'48,749',	'187,274',	'3.84'],
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
    # added6 = pdc.groups_to_json(groups=table6,  
    #     heading = paddy_heading)
    added7 = pdc.groups_to_json(groups=table7,  
        heading = paddy_heading)
    # added8 = pdc.groups_to_json(groups=table8,  
    #     heading = paddy_heading)
    added9 = pdc.groups_to_json(groups=table9,  
        heading = paddy_heading)

   
    data = added1+added2+added3+added4+added5+added7+added9
    paddy_data = [{'District': entry['District'],
                    'Spring_yield': entry['SpringYield'],
                    'Main_yield': entry['MainYield'],
                    'Total_yield': entry['TotalYield'],
                    } for entry in data]


    print(paddy_data)
    file_path1 = './data/2078_paddy_yield.json'
  

    with open(file_path1, 'w') as json_file:
        json.dump(paddy_data, json_file)

    return paddy_data



if __name__ == '__main__':
    paddy_yield()
    # millet_barley_yield()


