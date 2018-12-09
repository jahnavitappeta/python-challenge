import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    net_change = 0
    avg_change = 0
    greatest_increase = 0
    greatest_increase_month = ''
    greatest_decrease = 0
    greatest_decrease_month = ''

    net_amount = int(next(csvreader)[1])
    open_amount = net_amount
    close_amount = net_amount
    total_months = 1

    for row in csvreader:
        total_months += 1
        net_profit = int(row[1]) - close_amount
        close_amount = int(row[1])
        
        if(net_profit>greatest_increase):
            greatest_increase = net_profit
            greatest_increase_month = row[0]
        
        if(net_profit<greatest_decrease):
            greatest_decrease = net_profit
            greatest_decrease_month = row[0]


    net_change  = close_amount - open_amount
    avg_change = net_change/(total_months-1)
    
    fileContent = str(f'Financial Analysis\n')
    fileContent += str(f'----------------------------\n')
    fileContent = str(f'Total Months: {total_months}\n')
    fileContent += str(f'Total: ${net_amount}\n')
    fileContent += str(f'Average Change: ${round(avg_change,2)}\n')
    fileContent += str(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    fileContent += str(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})' )
    
    print(fileContent)
    file = open('output.txt',"w")
    file.write(fileContent)
    file.close()
        
