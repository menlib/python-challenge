import os
#Read the budget data from the csv file 

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


total_months=0
net_total_pl=0
profit_losses=[]
profit_losses_change=[]
average_pl_change=[]
date=[]
# print(csvpath)
with open(csvpath) as csvfile:
    
    # CSV reader specifies delimiter and variable that holds content 
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csvader}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_months=total_months+1
        net_total_pl=net_total_pl+ int(row[1])
        profit_losses.append(row[1])
        date.append(row[0])

    for each in range(1,len(profit_losses)):
        profit_losses_change.append(int(profit_losses[each])-int(profit_losses[each-1])) 

    average_pl_change = sum(profit_losses_change)/len(profit_losses_change)
    max_increase = max(profit_losses_change)
    max_decrease = min(profit_losses_change)                 
    max_increase_date = date[profit_losses_change.index(max_increase)+1]
    max_decrease_date = date[profit_losses_change.index(max_decrease)+1]
    formatted_max_increase ="(${})".format(max_increase)
    formatted_max_decrease ="(${})".format(max_decrease)
    rounded_average =round(average_pl_change,2)

    print("Financial Analysis")
    print("---------------------------")
    print("Total Months:" + " " + str(total_months))
    print("Total:" + " " + str(net_total_pl))
    # print(profit_losses_change)
    print("Average Change:" +" " + str(rounded_average))
    print("Greatest Increase in Profits:" + " " + max_increase_date + " " + str(("(${})").format(max_increase)))
    print("Greatest Decrease in Profits:" + " " + max_decrease_date + " " + str(("(${})").format(max_decrease)))