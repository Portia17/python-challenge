#get it to read CSV file
import os
import csv
csvpath = "Resources/budget_data.csv"

#print
print("Financial Analysis")
print("-------------------------------------------")

# open csv
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")

    csvheader = next(data)
    #print(f"CSV Header: {csvheader}")

    rowcount = 0
    for row in data:
        rowcount= rowcount + 1
    print("Total Months: " + str(rowcount))
    


       

     




#         #get number of months
#         months = len()
#         print ("Total Months: " + months)



# find total number of months