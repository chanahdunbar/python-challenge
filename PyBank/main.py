import os

# Module for reading CSV files
import csv

#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = os.path.join('Resources', 'budget_data.csv')
    
#Track variables
total_months = 0
total_profit_loss = 0
profit_loss_change = 0
previous_profit_loss = 0
greatest_increase = ["",0]
greatest_decrease = ["",9999999]
profit_loss_change_list = []

# Open & read csv file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    # reads the header row
    header = next(reader)

    # loop through
    for row in reader:
        # name for profit loss
        profit = int(row[1])
        month = row[0]

        # the total number of months included in the dataset
        total_months = total_months + 1

        # the net total amount of "Profit/Losses" over the entire period
        total_profit_loss = total_profit_loss + profit
        #print(row)

        if total_months != 1:
            # The changes in "Profit/Losses" over the entire period, and then the average of those changes
            profit_loss_change = profit - previous_profit_loss
            profit_loss_change_list.append(profit_loss_change)
            #profit_loss_change_list = profit_loss_change_list + profit_loss_change
            #dates = dates.append(month)
            #dates = dates + row["Date"]

            # The greatest increase in profits (date and amount) over the entire period
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[1] = profit_loss_change
                greatest_increase[0] = month
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[1] = profit_loss_change
                greatest_decrease[0] = month
        
        previous_profit_loss = profit

average_profit_loss = sum(profit_loss_change_list)/len(profit_loss_change_list)
print(average_profit_loss)

# Everything Printed
print(f"Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profit_loss}")
print(f"Average Change: {average_profit_loss}")
print(f"Greatest Increase in Profits: {greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease}")


