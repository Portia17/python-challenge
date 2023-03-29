
#get it to read CSV fil
import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")
output = os.path.join("analysis", "budget_analysis.txt")
#print


months = []
total = []
differences = []

# open csv
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    
    #read rows
    for row in data:
        #get month total from first column
        months.append(row [0])
        #making a list with all of the totals in the money column
        total.append(int(row[1]))
    
    # for the iteration were on starting after 1 to the length of the totals
    for i in range(1, len(total)):
        #make a list with the differences from the list total
        differences.append(total[i] - total[i - 1])
    

#getting numbers and assigning them to variables to print
month_count = len(months)
total_pl = sum(total)

#print(month_count)
#print(total_pl)

#get average
avg = round((sum(differences)/ len(differences)), 2)


#getting mins and maxes
p_max = max(differences)
p_min = min(differences)

#lining months up for mins and maxes
max_months = (months[differences.index(p_max) + 1])
min_months = (months [differences.index(p_min) + 1])


output_txt = (
    f"Financial Analysis\n"
    f"-------------------------------------------\n"
    f'Total months: {month_count}\n'
    f'Total Profit or Loss: ${total_pl}\n'
    f'Average Change: ${avg}\n'
    f'Greatest Increase in Profits: {max_months} (${p_max})\n'
    f'Greatest Decrease in Profits: {min_months} (${p_min})\n'
)

print(output_txt)
with open(output, 'w') as Bank:
    Bank.write(output_txt)
#print to a text file



     
