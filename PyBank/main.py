
#get it to read CSV fil
import csv

csvpath = "Resources/budget_data.csv"

#print
print("Financial Analysis")
print("-------------------------------------------")

months = []
total = []
differences = []

# open csv
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    

    for row in data:
        months.append(row [0])
        #making a list with all of the totals
        total.append(int(row[1]))
    
    # for the iteration were on starting after 1 to the length of the totals
    for i in range(1, len(total)):
        #make a list with the differences from the list total
        differences.append(total[i] - total[i - 1])
    

#total number 
#print(len(months))
month_count = len(months)
total_pl = sum(total)

print(month_count)
print(total_pl)

#get average
avg = round((sum(differences)/ len(differences)), 2)
print(avg)

p_max = max(differences)
p_min = min(differences)

max_months = (months[differences.index(p_max) + 1])
min_months = (months [differences.index(p_min) + 1])

print(max_months, p_max)
print(min_months, p_min)

# print("Total Months: " + str(rowcount))
# print("Total: " + "$" + str(price))      
# print("Average Change: " + "$" + str((avg)))
     
