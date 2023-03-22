#get it to read CSV file
import os
import csv
csvpath = "PyBank/Resources/budget_data.csv"

#print
print("Financial Analysis")
print("-------------------------------------------")

# open csv
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    data = list(data)

    rowcount = 0
    price = 0
    avg = 0
    for row in data:
        rowcount += 1
        price += int(row[1])
        
        for rowcount in data:
            avg += (((row[1]+1)+row[1])/rowcount)




print("Total Months: " + str(rowcount))
print("Total: " + "$" + str(price))      
print("Average Change: " + "$" + str((avg)))
     
