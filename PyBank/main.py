#Importing modules. os module allows us to create file paths and csv modules allows us to read csv files.
import os
import csv

#Create path for file name
csvpath = os.path.join("..","budget_data.csv")

#create lists to hold months and total profit loss values
new_months=[]
new_totalprofit=[]

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

        #Add months to months list
        new_months.append(row[0])

        #Add total profit to new list
        new_totalprofit.append(int(row[1]))

    #Print output    
    print('Financial Analysis')
    print('------------------------------')    
    print(f'Total Months: {totalmonths}')
    print(f'Total net profit/loss: ${totalprofit}')
    #print(new_months)
    #print(new_totalprofit)
    #print(new_totalprofit[1:])
    
    #create a new list to hold average change between consecutive profit/loss values
    diff_list = [j-i for i,j in zip(new_totalprofit,new_totalprofit[1:])]
    
    #Calculate average change and round it to decimals
    average_change=round(sum(diff_list)/len(diff_list),2)
    print(f'Average Change: $ {average_change}')

    #Calculate greatest increase and greatest decrease
    max_increase = max(diff_list)
    max_decrease = min(diff_list)

    #Find out the corresponding indexes for above variables
    ix_max = diff_list.index(max_increase)
    ix_min = diff_list.index(max_decrease)

    #Lookup corresponding months in new_months table 
    month_ix_max = new_months[ix_max+1]
    month_ix_min = new_months[ix_min+1]

    #Display max increase and max decrease in profit with their corresponding months 
    print(f'Greatest Increase in Profits: {month_ix_max} $({max_increase})')
    print(f'Greatest Decrease in Profits: {month_ix_min} $({max_decrease})')
    #print(new_months)
    #print(month_ix_max)
    #print(month_ix_min)

    #Redirect output of all print statements to a text file
    with open('PyBank_output.txt', 'w') as f:
        f.write('Financial Analysis' '\n'
            '------------------------------' '\n'
            f'Total Months: {totalmonths}' '\n'
            f'Total net profit/loss: ${totalprofit}' '\n'
            f'Average Change: ${average_change}' '\n'
            f'Greatest Increase in Profits: {month_ix_max} $({max_increase})' '\n'
            f'Greatest Decrease in Profits: {month_ix_min} $({max_decrease})')

