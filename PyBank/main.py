# Import necessary libraries
import pandas as pd
import os

# Define the file path to the budget data CSV file
file_path = 'Resources/budget_data.csv'

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(file_path)

# Calculate and print the total number of months
total_months = len(data)
print("Total Months: {}".format(total_months))

# Calculate and print the net total profit/loss
net_total = data['Profit/Losses'].sum()
print("Total: ${:,.0f}".format(net_total))

# Calculate the change in profit/loss for each month
data['Change'] = data['Profit/Losses'].diff()

# Calculate and print the average change in profit/loss
average_change = data['Change'].mean()
print("Average Change: ${:.2f}".format(average_change))

# Find and print the date and amount of the greatest increase in profits
greatest_increase_row = data.loc[data['Change'].idxmax()]
greatest_increase_date = greatest_increase_row['Date']
greatest_increase_amount = greatest_increase_row['Change']
print("Greatest Increase in Profits: {} (${:.0f})".format(greatest_increase_date, greatest_increase_amount))

# Find and print the date and amount of the greatest decrease in profits
greatest_decrease_row = data.loc[data['Change'].idxmin()]
greatest_decrease_date = greatest_decrease_row['Date']
greatest_decrease_amount = greatest_decrease_row['Change']
print("Greatest Decrease in Profits: {} (${:.0f})".format(greatest_decrease_date, greatest_decrease_amount))

# Define the path for the analysis text file
analysis_file_path = os.path.join('analysis', 'financial_analysis.txt')

# Create and write the analysis summary to the text file
analysis = "Financial Analysis\n" \
           "----------------------------\n" \
           "Total Months: {}\n" \
           "Total: ${:.0f}\n" \
           "Average Change: ${:.2f}\n" \
           "Greatest Increase in Profits: {} (${:.0f})\n" \
           "Greatest Decrease in Profits: {} (${:.0f})\n".format(
    total_months, net_total, average_change, greatest_increase_date, greatest_increase_amount,
    greatest_decrease_date, greatest_decrease_amount
)

with open(analysis_file_path, 'w') as txtfile:
    txtfile.write(analysis)
