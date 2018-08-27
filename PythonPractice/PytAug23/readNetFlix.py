# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'PytAug23', 'netflix_ratings.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module
showname = input("which show are you looking for?")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        name = row[0]
        rate = row[1]
        if name == showname:
            print(name+" is rated "+rate) 
            break
        else:
            print("no such video!")
            break            
    
    # Read each row of data after the header
#    for row in csvreader:
#        name = row[0]
#        rate = row[1]
#        if name == showname:
#            print(name+"is rated "+rate) 
#            break
#        else:
#            print("no such video!")
#            break            