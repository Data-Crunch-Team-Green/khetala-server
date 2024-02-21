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




def wheat_maize_yield():

    real_pg_no1 = pdc.page_number_converter(21)
    real_pg_no2 = pdc.page_number_converter(22)
    real_pg_no3 = pdc.page_number_converter(23)


    table1 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1',	'TAPLEJUNG',	'9,718',	'30,740',	'3.16',	'1,540',	'2,889',	'1.88'],
    ['1',	'SUNSARI',	'8,968',	'28,799',	'3.21',	'12,765',	'41,486',	'3.25'],
    8)  
    table2 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Madhesh',	'SAPTARI',	'3,930',	'12,920',	'3.29',	'15,317',	'53,300',	'3.48'],
    ['Madhesh',	'PARSA',	'4,589',	'18,566',	'4.05',	'21,998',	'81,758',	'3.72'],
    8)
    table3 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Bagmati',	'DOLAKHA',	'5730',	'17221',	'3.01',	'4246',	'7515',	'1.77'],
    ['Bagmati',	'KATHMANDU',	'5544',	'22939',	'4.14',	'2565',	'9148',	'3.57'],
    8)
    table4 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'NUWAKOT',	'15,952',	'60,239',	'3.78',	'4,495',	'17,044',	'3.79'],
    ['Bagmati',	'CHITWAN',	'26,019',	'98,644',	'3.79',	'5,151',	'23,248',	'4.51'],
    8)
    table5 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'MANANG',	'70',	'115',	'1.63',	'202',	'305',	'1.51',],
    ['Gandaki',	'BAGLUNG',	'19,863',	'65,680',	'3.31',	'6,900',	'17,319',	'2.51',],
    8)
    table6 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Lumbini',	'PALPA',	'21,230',	'55,562',	'2.62',	'5,795',	'14,660',	'2.53'],
    ['Lumbini',	'ARGHAKHANCHI',	'16,075',	'51,707',	'3.22',	'5,782',	'16,012',	'2.77'],
    8)  
    table7 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Lumbini',	'RUPANDEHI',	'3,145',	'10,693',	'3.4',	'26,118',	'103,167',	'3.95'],
    ['Lumbini',	'ROLPA',	'13,966',	'37,593',	'2.69',	'8,429',	'24,864',	'2.95',],
    8)  
    table8 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Karnali',	'DOLPA',	'2,359',	'3,749',	'1.59',	'3,000',	'4,010',	'1.34'],
    ['Karnali',	'MUGU',	'560',	'971',	'1.73',	'1,780',	'2,870',	'1.61'],
    8) 
    table9 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Karnali',	'HUMLA',	'149',	'274',	'1.84',	'1,072',	'1,526',	'1.42'],
    ['Karnali',	'SURKHET',	'14,943',	'46,256',	'3.1',	'12,191',	'41,354',	'3.39'],
    8) 
    table10 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Sudurpashchim',	'BAJURA',	'918',	'1,507',	'1.64',	'9,831',	'15,675',	'1.59'],
    ['Sudurpashchim',	'KANCHANPUR',	'3,378',	'9,248',	'2.74',	'31,210',	'99,995',	'3.14'],
    8) 

    headings = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield']

    added1 = pdc.groups_to_json(groups=table1,  
    heading = headings)
    added2 = pdc.groups_to_json(groups=table2,  
        heading = headings)
    added3 = pdc.groups_to_json(groups=table3,  
        heading = headings)
    added4 = pdc.groups_to_json(groups=table4,  
        heading = headings)
    added5 = pdc.groups_to_json(groups=table5,  
        heading = headings)
    added6 = pdc.groups_to_json(groups=table6,  
        heading = headings)
    added7 = pdc.groups_to_json(groups=table7,  
        heading = headings)
    added8 = pdc.groups_to_json(groups=table8,  
        heading = headings)
    added9 = pdc.groups_to_json(groups=table9,  
        heading = headings)
    added10 = pdc.groups_to_json(groups=table10,  
        heading = headings)

   
    data = added1+added2+added3+added4+added5+added6+added7+added8+added9+added10
    maize_data = [{'District': entry['District'],
                    'Maize_yield': entry['MaizeYield']
                    } for entry in data]

    wheat_data = [{'District': entry['District'],
                   'Wheat_yield': entry['WheatYield']
                   } for entry in data]
    print(wheat_data)
    print(maize_data)
    file_path1 = './data/maize_yield2078.json'
    file_path2 = './data/wheat_yield2078.json'

    with open(file_path1, 'w') as json_file:
        json.dump(maize_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(wheat_data, json_file)
    return wheat_data, maize_data




def millet_barley_yield():

    real_pg_no1 = pdc.page_number_converter(24)
    real_pg_no2 = pdc.page_number_converter(25)
    real_pg_no3 = pdc.page_number_converter(26)
    # real_pg_no4 = pdc.page_number_converter(24)


    table1 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1',	'TAPLEJUNG',	'3,041',	'4,252',	'1.40',	'113',	'143',	'1.27',	'269',	'405',	'1.51'],
    ['1',	'SUNSARI',	'505',	'585',	'1.16',	'319',	'314',	'0.99',	'14',	'22',	'1.57'],
    11)  
    table2 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Madhesh',	'SAPTARI',	'183',	'231',	'1.26',	'-',	'-',	'-',	'12',	'19',	'1.58'],
    ['Madhesh',	'DHANUSHA',	'176',	'180',	'1.02',	'-',	'-',	'-',	'7',	'9',	'1.29'],
    11)
    table3 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Madhesh',	'SARLAHI',	'709',	'638',	'0.90',	'-',	'-',	'-',	'62',	'71',	'1.14'],
    ['Madhesh',	'BARA',	'76',	'88',	'1.16',	'-',	'-',	'-',	'38',	'85',	'2.23'],
    11)

    table4 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Bagmati',	'DOLAKHA',	'3,675',	'5,221',	'1.42',	'935',	'876',	'1.21',	'136',	'165',	'0.94'],
    ['Bagmati',	'RAMECHAP',	'4,884',	'5,492',	'1.12',	'18',	'16',	'1.35',	'63',	'85',	'0.90'],
    11) 
    table5 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'SINDHULI',	'12,065',	'12,371',	'1.03',	'570',	'455',	'1.59',	'41',	'65',	'0.80'],
    ['Bagmati',	'CHITWAN',	'1,489',	'1,673',	'1.12',	'1,150',	'920',	'2.20',	'15',	'33',	'0.80'],
    11)
    table6 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'LAMJUNG',	'7,793',	'8,473',	'1.09',	'17',	'15',	'0.88',	'39',	'57',	'1.46'],
    ['Gandaki',	'BAGLUNG',	'18,456',	'23,247',	'1.26',	'87',	'115',	'1.33',	'644',	'1,133',	'1.76'],
    11)  
    table7 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Lumbini',	'PALPA',	'2,684',	'3,162',	'1.18',	'409',	'478',	'1.17',	'15',	'25',	'1.67'],
    ['Lumbini',	'RUPANDEHI',	'46',	'53',	'1.14',	'74',	'89',	'1.20',	'74',	'145',	'1.96'],
    11)  
    table8 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Lumbini',	'PYUTHAN',	'2,205',	'2,718',	'1.23',	'510',	'833',	'1.63',	'468',	'764',	'1.63'],
    ['Lumbini',	'ROLPA',	'1,126',	'1,298',	'1.15',	'548',	'625',	'1.14',	'551',	'654',	'1.19'],
    11) 
    table9 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Karnali',	'DOLPA',	'280',	'310',	'1.11',	'807',	'997',	'1.24',	'334',	'345',	'1.03'],
    ['Karnali',	'KALIKOT',	'1,241',	'1,362',	'1.10',	'123',	'142',	'1.15',	'821',	'1,297',	'1.58'],
    11) 

    table10 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Karnali',	'SALYAN',	'1,031',	'1,214',	'1.18',	'66',	'73',	'1.12',	'749',	'1,275',	'1.70'],
    ['Karnali',	'SURKHET',	'2,235',	'3,008',	'1.35',	'56',	'85',	'1.52',	'631',	'998',	'1.58'],
    11) 

    table11 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Sudurpashchim',	'BAJURA',	'2,521',	'2,575',	'1.02',	'45',	'57',	'0.79',	'973',	'1,228',	'1.26'],
    ['Sudurpashchim',	'KAILALI',	'356',	'404',	'1.13',	'24',	'28',	'0.89',	'176',	'275',	'1.56'],
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

    file_path1 = './data/millet_yield_2078.json'
    file_path2 = './data/buckwheat_yield_2078.json'
    file_path3 = './data/barley_yield_2078.json'
  
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



if __name__ == '__main__':
    # paddy_yield()
    millet_barley_yield()
    # wheat_maize_yield()
    # millet_barley_yield()


