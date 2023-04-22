#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote
candidate_dict = {}

import os

# Module for reading CSV files
import csv

#csvpath = os.path.join('..', 'Resources', 'election_data.csv')
csvpath = os.path.join('Resources', 'election_data.csv')

# Open & read csv file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # reads the header row
    header = next(reader)

    for row in reader:
        candidate = row[2]

        # if name has never been seen before, add to dictionary w/ a count of 1
        if candidate not in candidate_dict:
            # create the key & value
            candidate_dict[candidate] = 1

        # if name has been seen before, increment vote count
        else:
          candidate_dict[candidate] += 1  

#print(candidate_dict)

total_votes = sum(candidate_dict.values())
#print(total_votes)

winner_votes = 0
winner = ""

print("Election Results")
print("---------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------------------------------")

for key, value in candidate_dict.items():
    print(f"{key}: {(value/total_votes)*100}% ({value})")
    #print(value)
    if value > winner_votes:
        winner_votes = value
        winner = key

#print()
print("---------------------------------------------------")
print(f"Winner: {winner}")
#print(winner_votes)

# Write f-string