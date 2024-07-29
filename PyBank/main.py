import csv
import os

# Read the CSV file
csvpath= "Resources/budget_data.csv"
with open(csvpath,'r') as file:
    reader = csv.reader(file)
    next(reader)  

    months = []
    profitloss = []
    changes = []

    for row in reader:
        months.append(row[0])
        profitloss.append(int(row[1]))

total_months = len(months)

# Calculate the net total:
net_total = sum(profitloss)

# Calculate the changes in profit/losses and store them in a list
for i in range(1, total_months):
    change = profitloss[i] - profitloss[i-1]
    changes.append(change)

# Calculate the average change
average_change = sum(changes) / len(changes)

# Find the max increase and decrease:
max_increase = max(changes)
max_increase_date = months[changes.index(max_increase) + 1]
max_decrease = min(changes)
max_decrease_date = months[changes.index(max_decrease) + 1]

# Print the analysis results:
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

out_path = os.path.join("PyBank", "analysis", "result.txt")
with open(out_path, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n")

