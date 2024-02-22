from repo.pdf_to_data import PdfConverter
import json

pdc = PdfConverter


def paddy_yield():

    real_pg_no1 = pdc.page_number_converter(13)
    real_pg_no2 = pdc.page_number_converter(14)
    real_pg_no3 = pdc.page_number_converter(15)
   

    table1 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1',	'TAPLEJUNG',	'30',	'123',	'4.10',	'7,508',	'19,147',	'2.55',	'7,538',	'19,270',	'2.56'],
    ['1',	'SUNSARI',	'5,267',	'24,006',	'4.99',	'48,083',	'188,729',	'3.93',	'53,350',	'212,735',	'3.99',],
    11)  
    table2 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['2',	'SAPTARI',	'745',	'3,360',	'4.51',	'48,774',	'173,148',	'3.55',	'49,519',	'176,508',	'3.56'],
    ['2',	'PARSA',	'3,500',	'15,925',	'4.55',	'41,950',	'171,995',	'4.10',	'45,450',	'187,920',	'4.13'],
    11)
    table3 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Bagmati',	'SINDHUPALCHOK',	'3,200',	'14,368',	'4.49',	'8,781',	'21,179',	'2.41',	'11,981',	'35,547',	'2.97'],
    ['Bagmati',	'RAMECHAP',	'95',	'407',	'3.95',	'8,667',	'27,041',	'3.12',	'8,762',	'27,447',	'3.13'],
    11)

    table5 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'SINDHULI',	'1,145',	'5,233',	'5.10',	'12,802',	'47,495',	'3.71',	'13,947',	'52,728',	'3.78'],
    ['Bagmati',	'KAVRE',	'950',	'4,940',	'5.20',	'9,805',	'37,161',	'3.79',	'10,755',	'42,101',	'3.91'],
    11)
    table6 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'NUWAKOT',	'4,865',	'21,987',	'4.12',	'11,264',	'48,548',	'4.31',	'16,129',	'70,535',	'4.37'],
    ['Bagmati',	'CHITWAN',	'3,742',	'17,027',	'5.25',	'22,263',	'87,048',	'3.91',	'26,005',	'104,075',	'4.00'],
    11)  
    table7 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'GORKHA',	'589',	'2,656',	'4.51',	'10,606',	'35,954',	'3.39',	'11,195',	'38,611',	'3.45'],
    ['Gandaki',	'SYANGJA',	'490',	'2,259',	'4.61',	'15,603',	'64,596',	'4.14',	'16,093',	'66,855',	'4.15'],
    11)  
    table8 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'BAGLUNG',	'95',	'428',	'4.51',	'5,485',	'18,704',	'3.41',	'5,580',	'19,132',	'3.43'],
    ['Gandaki',	'NAWALPARASI EAST',	'560',	'2,545',	'5.12',	'20,794',	'82,760',	'3.98',	'21,354',	'85,305',	'3.99'],
    11) 
    table9 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Lumbini',	'PALPA',	'698',	'3,218',	'4.61',	'6,903',	'28,866',	'4.18',	'7,601',	'32,084',	'4.22'],
    ['Lumbini',	'BARDIYA',	'335',	'1,545',	'5.76',	'49,418',	'212,427',	'4.30',	'49,753',	'213,972',	'4.30'],
    11) 
    table10 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Sudurpashchim',	'BAJURA',	'25',	'95',	'3.81',	'4,175',	'10,405',	'2.49',	'4,200',	'10,500',	'2.50'],
    ['Sudurpashchim',	'KANCHANPUR',	'789',	'3,566',	'5.12',	'47,686',	'185,191',	'3.88',	'48,475',	'188,757',	'3.89'],
    11) 

    paddy_heading = ['Province', 'District', 'SArea', 'SProduction', 'SpringYield', 'MArea', 'MProduction', 'MainYield', 'TArea', 'TProduction', 'TotalYield']
    added1 = pdc.groups_to_json(groups=table1,  
    heading = paddy_heading )
    added2 = pdc.groups_to_json(groups=table2,  
        heading = paddy_heading)
    added3 = pdc.groups_to_json(groups=table3,  
        heading =paddy_heading)
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

   
    data = added1+added2+added3+added5+added6+added7+added9+added8+added10
    paddy_data = [{'District': entry['District'],
                    'Spring_yield': entry['SpringYield'],
                    'Main_yield': entry['MainYield'],
                    'Total_yield': entry['TotalYield'],
                    } for entry in data]


    print(paddy_data)
    file_path1 = './data/2077_paddy_yield.json'
  

    with open(file_path1, 'w') as json_file:
        json.dump(paddy_data, json_file)

    return paddy_data





def wheat_maize_yield():

    real_pg_no1 = pdc.page_number_converter(16)
    real_pg_no2 = pdc.page_number_converter(17)
    real_pg_no3 = pdc.page_number_converter(18)


    table1 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1',	'TAPLEJUNG',	'9,598',	'26,874',	'2.80',	'1,535',	'3,546',	'2.31',],
    ['1',	'SUNSARI',	'8,949',	'27,900',	'3.12',	'12,959',	'42,117',	'3.25',],
    8)  
    table2 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['2',	'SAPTARI',	'3,922',	'12,517',	'3.19',	'15,314',	'54,343',	'3.55'],
    ['2',	'PARSA',	'4,580',	'17,018',	'3.72',	'21,992',	'80,822',	'3.68'],
    8)
    table3 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['Bagmati',	'DOLAKHA',	'5,718',	'16,684',	'2.92',	'4,248',	'8,454',	'1.99'],
    ['Bagmati',	'LALITPUR',	'9,203',	'34,659',	'3.77',	'2,512',	'8,671',	'3.45'],
    8)
    table4 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'KATHMANDU',	'5,532',	'23,192',	'4.19',	'2,075',	'9,155',	'4.41'],
    ['Bagmati',	'CHITWAN',	'5,986',	'24,083',	'4.02',	'5,088',	'19,360',	'3.81',],
    8)
    table5 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'MANANG',	'70',	'111',	'1.59',	'202',	'305',	'1.51'],
    ['Gandaki',	'NAWALPARASIEAST',	'4,207',	'12,892',	'3.06',	'8,056',	'23,785',	'2.95'],
    8)
    table6 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Lumbini',	'PALPA',	'21,185',	'55,766',	'2.63',	'5,744',	'15,673',	'2.73'],
    ['Lumbini',	'ROLPA',	'13,438',	'34,482',	'2.57',	'8,407',	'24,884',	'2.96'],
    8)  
    table7 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Karnali',	'MUGU',	'589',	'941',	'1.60',	'3,201',	'3,986',	'1.25'],
    ['Karnali',	'SURKHET',	'15,011',	'43,844',	'2.92',	'13,941',	'42,425',	'3.04'],
    8)  
    table8 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Sudurpashchim',	'BAJURA',	'914',	'1,460',	'1.60',	'6,660',	'9,324',	'1.40'],
    ['Sudurpashchim',	'KANCHANPUR',	'3,271',	'8,959',	'2.74',	'34,554',	'133,032',	'3.85'],
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


   
    data = added1+added2+added3+added4+added5+added6+added7+added8
    maize_data = [{'District': entry['District'],
                    'Maize_yield': entry['MaizeYield']
                    } for entry in data]

    wheat_data = [{'District': entry['District'],
                   'Wheat_yield': entry['WheatYield']
                   } for entry in data]
    print(wheat_data)
    print(maize_data)
    file_path1 = './data/maize_yield2077.json'
    file_path2 = './data/wheat_yield2077.json'

    with open(file_path1, 'w') as json_file:
        json.dump(maize_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(wheat_data, json_file)
    return wheat_data, maize_data




def millet_barley_yield():

    real_pg_no1 = pdc.page_number_converter(19)
    real_pg_no2 = pdc.page_number_converter(20)
    real_pg_no3 = pdc.page_number_converter(21)
    real_pg_no4 = pdc.page_number_converter(22)


    table1 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1',	'TAPLEJUNG',	'3,008',	'4,181',	'1.39',	'270',	'402',	'1.49',	'103',	'140',	'1.36'],
    ['1',	'TERHATHUM',	'2,603',	'3,269',	'1.26',	'64',	'85',	'1.33',	'23',	'22',	'0.94'],
    11)  
    table2 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['1',	'BHOJPUR',	'5,429',	'6,980',	'1.29',	'12',	'17',	'1.43',	'35',	'32',	'0.89'],
    ['1',	'JHAPA',	'1,153',	'1,495',	'1.30',	'5',	'9',	'1.87',	'1,110',	'1,353',	'1.22'],
    11)
    table3 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['2',	'SAPTARI',	'181',	'227',	'1.25',	'-',	'-',	'-',	'-',	'-',	'-'],
    ['2',	'DHANUSHA',	'174',	'177',	'1.01',	'2',	'2',	'1.50',	'-',	'-',	'-'],
    11)

    table4 = pdc.converting_pdf_to_table_data(real_pg_no1, 
    ['2',	'SARLAHI',	'702',	'627',	'0.89',	'62',	'71',	'1.14',	'-',	'-',	'-'],
    ['2',	'BARA',	'75',	'87',	'1.15',	'38',	'85',	'2.23',	'-',	'-',	'-'],
    11) 
    table5 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Bagmati',	'DOLAKHA',	'3,635',	'5,133',	'1.41',	'146',	'175',	'1.20',	'901',	'1,097',	'1.22'],
    ['Bagmati',	'CHITWAN',	'1,473',	'1,645',	'1.12',	'18',	'34',	'1.87',	'70',	'77',	'1.10'],
    11)
    table6 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    ['Gandaki',	'MANANG',	'-',	'-',	'-',	'109',	'189',	'1.73',	'262',	'491',	'1.88'],
    ['Gandaki',	'SYANGJA',	'15,926',	'20,004',	'1.26',	'4',	'6',	'1.65',	'221',	'220',	'1.00'],
    11)  
    table7 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Gandaki',	'MYAGDI',	'2,530',	'3,296',	'1.30',	'279',	'372',	'1.33',	'144',	'142',	'0.99'],
    ['Gandaki',	'NAWALPARASI EAST',	'256',	'287',	'1.12',	'8',	'10',	'1.25',	'80',	'79',	'0.99'],
    11)  
    table8 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Lumbini',	'PALPA',	'2,655',	'3,109',	'1.17',	'19',	'35',	'1.83',	'410',	'407',	'0.99'],
    ['Lumbini',	'ROLPA',	'1,113',	'1,276',	'1.15',	'556',	'661',	'1.19',	'108',	'98',	'0.91'],
    11) 
    table9 = pdc.converting_pdf_to_table_data(real_pg_no3, 
    ['Karnali',	'DOLPA',	'277',	'305',	'1.10',	'354',	'355',	'1.00',	'646',	'679',	'1.05'],
    ['Karnali',	'RUKUM WEST',	'461',	'623',	'1.35',	'413',	'518',	'1.25',	'-',	'-',	'-'],
    11) 

    table10 = pdc.converting_pdf_to_table_data(real_pg_no4, 
    ['Karnali',	'SALYAN',	'1,020',	'1,194',	'1.17',	'950',	'1,276',	'1.34',	'60',	'71',	'1.19'],
    ['Karnali',	'SURKHET',	'2,215',	'2,957',	'1.34',	'931',	'1,424',	'1.53',	'-',	'-',	'-'],
    11) 

    table11 = pdc.converting_pdf_to_table_data(real_pg_no4, 
    ['Sudurpashchim',	'BAJURA',	'2,494',	'2,531',	'1.02',	'976',	'990',	'1.01',	'7',	'11',	'1.54'],
    ['Sudurpashchim',	'KAILALI',	'352',	'398',	'1.13',	'176',	'370',	'2.10',	'22',	'27',	'1.22'],
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
    file_path1 = './data/millet_yield2077.json'
    file_path2 = './data/buckwheat_yield2077.json'
    file_path3 = './data/barley_yield2077.json'

    with open(file_path1, 'w') as json_file:
        json.dump(millet_data, json_file)
    with open(file_path2, 'w') as json_file:
        json.dump(buckwheat_data, json_file)
    with open(file_path3, 'w') as json_file:
        json.dump(barley_data, json_file)
    return millet_data, buckwheat_data, barley_data




if __name__ == '__main__':
    millet_barley_yield()
    # wheat_maize_yield()
    # paddy_yield()
