# modules
import os
import csv

# set path for csv
csvpath = os.path.join("Resources", "budget_data.csv")

# set variables
months = []
profit_loss = []
difference = []
greatest_inc_date = ""
greatest_dec_date = ""

# open and read the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # count total months
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

for i in range(1, len(profit_loss)):

# find average change
    difference.append(profit_loss[i] - profit_loss[i-1])
    avg_chg = sum(difference) / len(difference)

# find greatest (increase & date) + (decrease & date)
    greatest_inc = max(difference)
    greatest_inc_date = str(months[difference.index(max(difference))])

    greatest_dec = min(difference)
    greatest_dec_date = str(months[difference.index(min(difference))])

# print statements
print("Financial Analysis")
print("-------------------------------")
print("Total Months: ", len(months))
print("Net Total: $", sum(profit_loss))
print("Average Change: $", round(avg_chg, 2))  
print("Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")")
print("Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")")

# print to text
print("Financial Analysis", file=open("output.txt", "a"))
print("-------------------------------", file=open("output.txt", "a"))
print("Total Months: ", len(months), file=open("output.txt", "a"))
print("Net Total: $", sum(profit_loss), file=open("output.txt", "a"))
print("Average Change: $", round(avg_chg, 2), file=open("output.txt", "a"))  
print("Greatest Increase: ", greatest_inc_date, "($", greatest_inc,")", file=open("output.txt", "a"))
print("Greatest Decrease: ", greatest_dec_date, "($", greatest_dec,")", file=open("output.txt", "a"))