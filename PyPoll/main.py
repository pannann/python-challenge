# Import necessary libraries
import pandas as pd
import os

# Define the file path to the election data CSV file
file_path = "Resources\election_data.csv"

# Read the CSV file into a Pandas DataFrame
data = pd.read_csv(file_path)

# Calculate and print the total number of votes
total_votes = len(data)
print("Election Results")
print("-" * 25)
print("Total Votes: {}".format(total_votes))
print("-" * 25)

# Group the data by candidate and count the votes for each candidate
candidate_votes = data["Candidate"].value_counts()

# Calculate the percentage of votes each candidate won
candidate_percentages = (candidate_votes / total_votes) * 100

# Find and print the winner based on popular vote
winner = candidate_votes.idxmax()

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(candidate + ": {:.3f}% ({})".format(percentage, votes))

print("-" * 25)
print("Winner: " + winner)
print("-" * 25)

# Define the path for the analysis text file
analysis_file_path = os.path.join('analysis', 'election_results.txt')

# Create and write the analysis summary to the text file
analysis_text = []
analysis_text.append("Election Results")
analysis_text.append("-------------------------")
analysis_text.append("Total Votes: " + str(total_votes))
analysis_text.append("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    result_line = candidate + ": {:.3f}% ({})".format(percentage, votes)
    analysis_text.append(result_line)

analysis_text.append("-------------------------")
analysis_text.append("Winner: " + winner)
analysis_text.append("-------------------------")

with open(analysis_file_path, "w") as txtfile:
    for line in analysis_text:
        txtfile.write(line + "\n")
