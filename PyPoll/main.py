#get it to read csv

import os
import csv

csvpath = "Resources/election_data.csv"
output = os.path.join("analysis", "election_analysis.txt")

d_candidates = {}
l_candidates= []
total_votes = 0
winner = ""
winning_votes = 0
percent = []

with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    next(data)

    for row in data:
        total_votes += 1
        if row[2] not in l_candidates:
            l_candidates.append(row[2])
            #key = value ie candidate : 1
            d_candidates[row[2]] = 0
        d_candidates[row [2]] += 1


print(d_candidates)


# output_txt = (
#     f'Election Results\n'
#     f'-------------------------\n'
#     f'Total Votes: {total_votes}\n'
#     f'-------------------------\n'
#)


# for person in d_candidates:
#     candidate_votes = d_candidates.get(person)
#     # d_candidates[person]
#     votes_percent = candidate_votes / total_votes * 100
#     stmt = f'{person}: {votes_percent:.3f}%: {candidate_votes} '
#     print(stmt)
            
            
#     if candidate_votes > winning_votes:
#         winning_votes = candidate_votes
#         winner = person

# print (winner)


# with open(output, 'w') as outfile:
#     outfile.write(
#         f'Election Results\n'
#         f'-------------------------\n'
#         f'Total Votes: {total_votes}\n'
#         f'-------------------------\n'
#         f'{d_candidates}'
#         f'-------------------------\n'
#         f'Winner: {winner}'
#     )
    
    #print and write results

    #loop to print candidate votes

        #print candidate and their votes

        #if statement to see if they win
            #if votes > winner votes, set name as winner


    #print winner
            







    

    