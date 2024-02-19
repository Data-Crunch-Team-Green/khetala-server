
import PyPDF3
import pandas as pd
import json

'''
output expected: 
{'Belt': ['Mountain', 'Hill', 'Terai'], 
'Area ( Square Km.)': ['51,817', '61,345', '34,019'], 
'Percentage': ['35', '42', '23']}
'''



'''
Limitations - 
1. Duplicated start_chr or end_chr
2. does not deal with merged rows
3. empty cells not taken care of
4. wrapped cells

Only work for - 
1. all rows are filled no empty cell no merged cells, khali ma '-' bhaye ni chalxa

'''

"""Expected output:
[
{ 'district': 0,  'spring_yield'  : 4.14, 'main_yield' : 3.01, 'total_yield': 3.02},
{ 'district': 0, 'spring_yield' : 4.34, 'main_yield' : 2.42, 'total_yield': 3.02},
...
]

[[{}]]


district = [{ 'name' : 'Taplejung', 'nepName': 'ताप्लेजुङ' },
            { 'name' : 'Jhapa', 'nepName': ‘झापा’ }, ...]

"""
def converting_pdf_to_table_data(page_number: int, starting_chr: list, ending_chr: list, total_columns: int) -> list:
    open_file = open('./data/report.pdf','rb' )
    reader = PyPDF3.PdfFileReader(open_file)
    print(reader.numPages)

    pages = reader.getPage(page_number)
    
    extracted_pages = pages.extractText()
   
    l = extracted_pages.split('\n')

    base_a = 0
    table_data = []
    end = 0 
    columns_lst = total_columns-1
    
    for a in range(columns_lst,len(l)):
        first =a-columns_lst
        second = a+1
        j = l[first:second]
        words = [x.strip() for x in j]
        # print(f"{a}\n {words} \n {ending_chr} \n")        
        if words == ending_chr:
            end += a 
            break 
    t = end + total_columns
    starter = 0
    for a in range(columns_lst, t):
        first = a-columns_lst
        second = a+1
        sublist = l[first:second]
        stripped = [x.strip() for x in sublist]
        if stripped == starting_chr:
            table_data.append(stripped)
            base_a = a
            
        if base_a != 0:
            if a > base_a:
                starter+=1
                if starter%total_columns==0:
                    table_data.append(stripped)           


    return table_data


def groups_to_json(groups : list, heading):
    data = groups
    naya_list = []
    
  
    for a in data:
        diction = {}
        for i in range(len(heading)):        
            diction[heading[i]]= a[i]
            if i == len(heading)-1:
                naya_list.append(diction)
    return naya_list
                


def page_number_converter(page_number: str):
    real_pg = page_number - 1 + 10
    return real_pg




def final():

    real_pg_no1 = page_number_converter(18)
    real_pg_no2 = page_number_converter(19)
    real_pg_no3 = page_number_converter(20)


    table1 = converting_pdf_to_table_data(real_pg_no1, 
    ['KOSHI', 'TAPLEJUNG','11,198','38,312', '3.42', '1,537', '2,875', '1.87'],
    ['KOSHI', 'SUNSARI', '9,034', '29,432', '3.26', '12,127', '41,195', '3.40'],
    8)  
    table2 = converting_pdf_to_table_data(real_pg_no1, 
    ['MADHESH', 'SAPTARI','6,589', '23,211', '3.52', '15,017', '54,351', '3.62'],
    ['MADHESH', 'PARSA', '4,189', '17,166', '4.10', '23,008', '86,163', '3.74'],
    8)
    table3 = converting_pdf_to_table_data(real_pg_no1, 
    ['BAGMATI', 'DOLAKHA','6,171', '22,155', '3.59', '4,246', '7,515', '1.77'],
    ['BAGMATI', 'BHAKTAPUR', '1,900', '7,750', '4.08', '3,150', '12,409', '3.94'],
    8)
    table4 = converting_pdf_to_table_data(real_pg_no2, 
    ['BAGMATI', 'LALITPUR','8,573', '33,656', '3.93', '3,485', '11,858', '3.40'],
    ['BAGMATI', 'CHITWAN', '28,055', '105,239', '3.75', '5,151', '23,248', '4.51'],
    8)
    table5 = converting_pdf_to_table_data(real_pg_no2, 
    ['GANDAKI', 'MANANG','177', '351', '1.98', '213', '500', '2.35'],
    ['GANDAKI', 'NAWALPARASI EAST', '5,101', '15,556', '3.05', '7,605', '20,930', '2.75'],
    8)
    table6 = converting_pdf_to_table_data(real_pg_no3, 
    ['KARNALI', 'DOLPA','2,204','2,798', '1.27', '2,805', '4,010', '1.43'],
    ['KARNALI', 'SURKHET', '13,252', '46,756', '3.53', '12,191', '42,354', '3.47'],
    8)  
    table7 = converting_pdf_to_table_data(real_pg_no3, 
    ['SUDURPASHCHIM', 'BAJURA', '3,293','4,850', '1.47', '10,450', '15,675', '1.50'],
    ['SUDURPASHCHIM', 'KANCHANPUR', '3,250', '11,534', '3.55', '31,355', '101,995', '3.25'],
    8)  
    table8 = converting_pdf_to_table_data(real_pg_no2, 
    ['LUMBINI', 'PALPA', '21,643','55,779', '2.58', '5,786', '13,572', '2.35'],
    ['LUMBINI', 'ARGHAKHANCHI', '16,955', '54,975', '3.24', '7,340', '19,955', '2.72'],
    8) 
    table9 = converting_pdf_to_table_data(real_pg_no2, 
    ['LUMBINI', 'RUPANDEHI', '2,751','10,752', '3.91', '26,118', '103,167', '3.95'],
    ['LUMBINI', 'ROLPA', '12,335', '38,500', '3.12', '8,596', '24,400', '2.84'],
    8) 

    added1 = groups_to_json(groups=table1,  
    heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added2 = groups_to_json(groups=table2,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added3 = groups_to_json(groups=table3,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added4 = groups_to_json(groups=table4,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added5 = groups_to_json(groups=table5,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added6 = groups_to_json(groups=table6,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added7 = groups_to_json(groups=table7,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added8 = groups_to_json(groups=table8,  
        heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])
    added9 = groups_to_json(groups=table9,  
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



if __name__ == '__main__':
    final()


        # table = converting_pdf_to_table_data(real_pg_no, 
    #         ['LUMBINI', 'PALPA','21,643', '55,779', '2.58', '5,786', '13,572', '2.35'],
    #         ['LUMBINI', 'ROLPA', '12,335', '38,500', '3.12', '8,596', '24,400', '2.84'],
    #         8)
    # grouped = data_to_groups(table_data=table, columns=11)
    # groups_to_json(groups=table,  
    #                heading = ['Province', 'District', 'S.Area', 'S.Production', 'S.Yield', 'M.Area', 'M.Production', 'M.Yield', 'T.Area', 'T.Production', 'T.Yield'])
    # groups_to_json(groups=table,  
    #         heading = ['Province', 'District', 'MaizeArea', 'MaizeProduction', 'MaizeYield', 'WheatArea', 'WheatProduction', 'WheatYield'])

  