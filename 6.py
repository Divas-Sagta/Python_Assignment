
"""
- Write a Python script which reads a csv file and Visualizes a table with proper indentations and borders
(make sure to don’t use any table making module or package).

Example : CSV file like this:

Name,Age,Department
Alice,30,HR
Bob,25,Engineering
Charlie,35,Marketing
Diana,28,Sales

"""

import csv

def read_csv(filename):
    """Reads a CSV file and returns the data as a list of lists."""
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]  # Read all rows into a list
    return data

def get_max_widths(data):
    """Finds the maximum width of each column."""
    num_columns = len(data[0])  
    maxcol_width = []  

    for i in range(num_columns):  
        max_width = 0  

        for row in data: 
            cell_length = len(row[i])  
            if cell_length > max_width:
                max_width = cell_length  
        
        maxcol_width.append(max_width)  
    
    return maxcol_width

def horiline(maxcol_width):
    print("+", end="")
    for width in maxcol_width:
        print("-" * (width + 2) + "+", end="")
    print()

def print_table(data):
    maxcol_width = get_max_widths(data) 
    
    horiline(maxcol_width) 
    
    row_index = 0
    for row in data:
        print("|", end="")
        col_index = 0
        for col in row:
            print(f" {col.ljust(maxcol_width[col_index])} |", end="")  
            col_index += 1
        print()
        
        if row_index == 0: 
            horiline(maxcol_width)
        
        row_index += 1  
    
    horiline(maxcol_width) 

filename = "data.csv"  
data = read_csv(filename)
print_table(data)

