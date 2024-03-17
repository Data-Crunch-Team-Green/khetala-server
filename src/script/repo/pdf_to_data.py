
import PyPDF3
import csv
import re


class FormatConverter:  
    '''
    Convert the pdf or csv file into json format. This is for the yield data obtained from MoALD.
    '''

    def converting_pdf_to_table_data(filepath, page_number: int) -> list:
        '''
        Extracting the pdf page.
        
        Parameters:
        filepath (str): Filepath to the pdf file
        page_number (int): Page number of the pdf you want to extract

        Returns:
        extracted_file_in_list (list) : Returns the pdf page in list format
        '''
        
        open_file = open(filepath,'rb' )
        reader = PyPDF3.PdfFileReader(open_file)
        print(reader.numPages)

        pages = reader.getPage(page_number)
        
        extracted_pages = pages.extractText() 
        l = re.split(r'\n', extracted_pages)
        return l 
    
    
    def converting_csv_to_table_data(filepath):
        '''
        Converting csv file. 
        Parameters:
        filepath (str): Filepath to the csv file
        Returns:
        extracted_file_in_list (list) : Returns the csv file in list format
        '''
        data = []
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                for a in row:
                    data.append(a)
        print(data)
        return data
    

    def filtering_needed_data(extracted_data, starting_chr: list, ending_chr: list, total_columns: int):
        '''
        Filters the required yield data from extracted file and groups them according to the column. 
        Parameters:
        starting_chr (list): List of the first row of the yield table.
        ending_chr (list): List of the last row of the yield table.
        total_column (list): Total column in the yield table, used for grouping district data.
        Returns:
        table_data : Returns list of grouped yield data as per district
        '''
        base_a = 0
        table_data = []
        end = 0 
        columns_lst = total_columns-1
        
        for a in range(columns_lst,len(extracted_data)):
            first =a-columns_lst
            second = a+1
            j = extracted_data[first:second]
            words = [x.strip() for x in j]      
            if words == ending_chr:
                end += a 
                break 
        t = end + total_columns
        starter = 0
        for a in range(columns_lst, t):
            first = a-columns_lst
            second = a+1
            sublist = extracted_data[first:second]
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
        '''
        Converts the filtered data into json.
        Parameters:
        groups (list): Data that had been filtered and grouped
        heading (list): Heading of the columns used as keys
        Returns:
        naya_list(list) : Provides the grouped data in json format
        '''
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
        real_pg = page_number -1
        return real_pg




