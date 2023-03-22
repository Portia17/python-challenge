#get it to read csv
import os
import csv
csvpath = "Resources/election_data.csv"

with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)
    data = list(data)

    rowcount = 0
    price = 0
    change = 0
    for row in data:
        rowcount += 1