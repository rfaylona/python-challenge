# modules
import os
import csv

#set path for csv
csvpath = os.path.join("Resources", "election_data.csv")

# set variables
candidates_name = {}
count = 0
votes = 0
percent_of_votes = 0
most_votes = 0
most_voted = ""

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        candidate = row[2]
        count += 1
        if candidate in candidates_name.keys():
            candidates_name[candidate] += 1
        else:
            candidates_name[candidate] = 1
    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")
    
    for candidate in candidates_name:
        votes += candidates_name[candidate]

        percent_of_votes = (candidates_name[candidate])/(count) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {votes}")

        if candidates_name[candidate] > most_votes:
            most_voted = candidate
            most_votes = candidates_name[candidate]

print("-------------------------")
print(f"Winner: {most_voted}")
print("-------------------------")