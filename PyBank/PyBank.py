import os 
import csv 


#locate directory
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

#open directory
pybank_path = os.path.join (dir_path, "Resources")
print(pybank_path)
print(type(pybank_path))
os.chdir(pybank_path)

#empty lists 

#include total profit
profit = []
#month to month changes
monthly_changes = []
#date associated with month to month changes
date = []

#variables 
monthtotal = 0
nettotal = 0
profit = 0
initial_profit = 0
total_changes_profits = 0
#read csv file 
with open ("budget_data.csv", "r") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)
    #skip header
    next(csvreader)

    #read each row of data after the header 
    for row in csvreader:
        #month total and net total of the profits/losses and dates
        monthtotal += 1
        nettotal += float(row[1])
        date.append(row[0])

        #profits/losses 
        final_profit = int(row[1])
        profit_monthly_changes = final_profit - initial_profit
        monthly_changes.append(profit_monthly_changes)

        #find monthly changes 
        total_changes_profits += profit_monthly_changes
        initial_profit= final_profit

        #find average of the changes between the profits and losses month to month 
        profits_average_change = sum(monthly_changes)/(monthtotal)

        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase)]
        decrease_date = date[monthly_changes.index(greatest_decrease)]

        


print ("Financial Analysis:")
print ("---------------------")
print (f' total months: {monthtotal}')
print (f' Total: ${nettotal}')
print(f' Average Change : ${round(profits_average_change)}')
print (f' Greatest Increase in Profits : {increase_date} $({greatest_increase})')
print(f' Greatest Decrease in Profits : {decrease_date} $({greatest_decrease})')

pybank_path_write = os.path.join(dir_path, 'analysis')
os.chdir(pybank_path_write)

with open ("pybank_analysis.txt", "w") as text: 
    text.write ("Financial Analysis: \n")
    text.write ("--------------------- \n")
    text.write (f' Total months: {monthtotal}\n')
    text.write (f' Total: ${nettotal}\n')
    text.write(f' Average Change : ${round(profits_average_change)}\n')
    text.write (f' Greatest Increase in Profits : {increase_date} $({greatest_increase})\n')
    text.write(f' Greatest Decrease in Profits : {decrease_date} $({greatest_decrease})\n')
