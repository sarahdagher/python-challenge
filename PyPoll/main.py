#poll

import csv
import os

election_data = "election_data_1.csv" and "election_data_2.csv"
output_path = election_summary
votes = 0
winners_votes = 0
sum_candidates = 0
most_votes = ["",0]
options_candidates = []
votes_candidates = {}

with open(election_data) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        votes = votes + 1
        sum_candidates = row["Candidate"]

        if row ["Candidate"] not in options_candidates:
            options_candidates.append(row["Candidate"]) = 1

        else: 
            votes_candidates[row["Candidate"]] = votes_candidates[row["Candidate"]] + 1

    print()
    print()
    print()
    Print("Election Results")
    Print("-----------------------------------------------")
    print("Total Votes" + str(votes))
    print("-----------------------------------------------")
    for candidate in votes_candidates:
        print(candidate + " " + str(round(((votes_candidates[candidate]/votes)*100))) + "%") " (" + str(votes_candidates[candidate]) + ")") 
    candidate_results = (candidate + " " + str(round(((votes_candidates[candidate]/votes)*100))) + "%" + " (" + str(votes_candidates[candidate]) + ")") 
    
votes_candidates

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

print("--------------------------------------------------")
print("Winner: " + str(winner[0]))
print("--------------------------------------------------")


