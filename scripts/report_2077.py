from repo.pdf_to_data import PdfConverter
import json

pdc = PdfConverter


def paddy_yield():

    real_pg_no1 = pdc.page_number_converter(13)
    real_pg_no2 = pdc.page_number_converter(14)
    real_pg_no3 = pdc.page_number_converter(15)
    # real_pg_no4 = pdc.page_number_converter(20)


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

    # table4 = pdc.converting_pdf_to_table_data(real_pg_no2, 
    # ['Bagmati',	'NUWAKOT',	'5,486',	'22,383',	'4.08',	'11,612',	'47,029',	'4.05',	'17,098',	'69,411',	'4.06'],
    # ['Bagmati',	'CHITWAN',	'4,210',	'19,055',	'4.53',	'24,247',	'94,321',	'3.89',	'28,457',	'113,376',	'3.98'],
    # 11)
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
    # added4 = pdc.groups_to_json(groups=table4,  
    #     heading = paddy_heading)
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

if __name__ == '__main__':
    paddy_yield()
