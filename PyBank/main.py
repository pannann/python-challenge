import pandas as pd
import os

file_path = 'Resources/budget_data.csv'
data = pd.read_csv(file_path)
#print(data)
#The total number of months included in the dataset
total_months = len(data)
output = "Total Months: {}".format(total_months)
print(output)
net_total = data['Profit/Losses'].sum()
output2 = "Total: ${:,.0f}".format(net_total)
print(output2)
data['Change'] = data['Profit/Losses'].diff()
# Calculate the average change in "Profit/Losses" (excluding the first row, which contains NaN)
average_change = data['Change'].mean()
output3 = "Average Change: ${:.2f}".format(average_change)
print(output3)
# Find the row with the greatest increase in profits
greatest_increase_row = data.loc[data['Change'].idxmax()]

# Extract the date and amount of the greatest increase
greatest_increase_date = greatest_increase_row['Date']
greatest_increase_amount = greatest_increase_row['Change']

greatest_increase_output = "Greatest Increase in Profits: {} (${:.0f})".format(
    greatest_increase_date, greatest_increase_amount
)
print(greatest_increase_output)

greatest_decrease_row = data.loc[data['Change'].idxmin()]

# Extract the date and amount of the greatest decrease
greatest_decrease_date = greatest_decrease_row['Date']
greatest_decrease_amount = greatest_decrease_row['Change']

greatest_decrease_output = "Greatest Decrease in Profits: {} (${:.0f})".format(
    greatest_decrease_date, greatest_decrease_amount
)
print(greatest_decrease_output)

analysis_file_path = os.path.join('analysis', 'financial_analysis.txt')

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

