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

# count votes per candidate
    for row in csvreader:
        # identify candidates to count votes
        candidate = row[2]
        count += 1
        if candidate in candidates_name.keys():
            candidates_name[candidate] += 1
        else:
            candidates_name[candidate] = 1
# print results    
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")
# print to text
    print("Election Results", file=open("output.txt", "a"))
    print("-------------------------", file=open("output.txt", "a"))
    print(f"Total Votes: {count}", file=open("output.txt", "a"))
    print("-------------------------", file=open("output.txt", "a"))
# identify most voted  
    for candidate in candidates_name:
        votes += candidates_name[candidate]

        percent_of_votes = (candidates_name[candidate])/(count) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {votes}")
        print(f"{candidate}: {int(percent_of_votes)}% {votes}", file=open("output.txt", "a"))

        if candidates_name[candidate] > most_votes:
            most_voted = candidate
            most_votes = candidates_name[candidate]

print("-------------------------")
print(f"Winner: {most_voted}")
print("-------------------------")

print("-------------------------", file=open("output.txt", "a"))
print(f"Winner: {most_voted}", file=open("output.txt", "a"))
print("-------------------------", file=open("output.txt", "a"))