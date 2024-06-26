import os
import csv

budget_data = os.path.join(r"C:\Users\ccana\Downloads\python-challenge-main\python-challenge-main\PyBank\Resources\budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader: 

        dates.append(row[0])

        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        total_months += 1

        total_pl = total_pl + int(row[1])

    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index] 

    avg_change = sum(profits)/len(profits)


print("Financial Analysis")
print("-------")
print(f"Total Months: {str(total_months)}")
print(f"total : ${str(total_pl)}")
print(f"Total: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt", "w")


line1 = "Financial Analysis"
line2 = "-------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = (f"total : ${str(total_pl)}")
line5 = (f"Total: ${str(round(avg_change,2))}")
line6 = (f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = (f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))




