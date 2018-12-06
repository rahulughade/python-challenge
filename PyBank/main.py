#Importing modules. os module allows us to create file paths and csv modules allows us to read csv files.
import os
import csv

#Create path for file name
csvpath = os.path.join("..","budget_data.csv")

#Read csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first    
    csv_header = next(csvreader)
    
    #Create and initialize variables
    totalprofit = 0
    totalmonths = 0

    #Loop through csv data to calculate total months and total net profit
    for row in csvreader:
        totalmonths += 1
        totalprofit += int(row[1])
    print('Financial Analysis')
    print('------------------------------')    
    print(f'Total Months: {totalmonths}')
    print(f'Total net profit/loss: ${totalprofit}')