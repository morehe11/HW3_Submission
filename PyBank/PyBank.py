import os 
import csv 


#locate directory
dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

pybank_path = os.path.join (dir_path, "Resources")
print(pybank_path)
print(type(pybank_path))
os.chdir(pybank_path)


with open ("budget_data.csv", "r") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)
    #skip header
    next(csvreader)

    monthtotal = 0
    nettotal = 0

    #read each row of data after the header 
    for row in csvreader:
        monthtotal += 1
        nettotal += float(row[1])
        averagechange = nettotal/monthtotal
        increase = max(row[1])
        decrease= min(row[1])


print ("Financial Analysis: =")
print ("---------------------")
print (f' total months: {monthtotal}')
print (f' Total: ${nettotal}')
print (f'Average: {averagechange}')
print (f'Greatest increase: {increase}')
print (f' Greatest Decrease: {decrease}')   

