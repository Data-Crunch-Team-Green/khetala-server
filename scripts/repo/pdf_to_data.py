
import PyPDF3
import pandas as pd
import re


class PdfConverter:
    
    def converting_pdf_to_table_data(page_number: int, starting_chr: list, ending_chr: list, total_columns: int) -> list:
        open_file = open('./data/report.pdf','rb' )
        reader = PyPDF3.PdfFileReader(open_file)
        print(reader.numPages)

        pages = reader.getPage(page_number)
        
        extracted_pages = pages.extractText()
    
        # l = extracted_pages.split('\n')
  
        l = re.split(r'\s+|\n+', extracted_pages)
 

        base_a = 0
        table_data = []
        end = 0 
        columns_lst = total_columns-1
        
        for a in range(columns_lst,len(l)):
            first =a-columns_lst
            second = a+1
            j = l[first:second]
            words = [x.strip() for x in j]      
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
                    


    def page_number_converter(page_number: int):
        # real_pg = page_number - 1 + 9
        real_pg = page_number + 7
        return real_pg


