import pandas as pd
import os

# Define the file path to the election data CSV file
file_path = "Resources\election_data.csv"
data = pd.read_csv(file_path)
total_votes = len(data)
print("Election Results")
print("-" * 25)
output = "Total Votes: {}".format(total_votes)
print(output)
print("-" * 25)

candidate_votes = data["Candidate"].value_counts()

candidate_percentages = (candidate_votes / total_votes) * 100

winner = candidate_votes.idxmax()

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(candidate + ": {:.3f}% ({})".format(percentage, votes))

print("-" * 25)
print("Winner: " + winner)
print("-" * 25)

analysis_text = []
analysis_text.append("Election Results")
analysis_text.append("-------------------------")
analysis_text.append("Total Votes: " + str(output))
analysis_text.append("-------------------------")

for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    result_line = candidate + ": {:.3f}% ({})".format(percentage, votes)
    analysis_text.append(result_line)

analysis_text.append("-------------------------")
analysis_text.append("Winner: " + winner)
analysis_text.append("-------------------------")

analysis_file_path = os.path.join('analysis', 'election_results.txt')

with open(analysis_file_path, "w") as txtfile:
    for line in analysis_text:
        txtfile.write(line + "\n")