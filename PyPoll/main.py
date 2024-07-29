import csv
import os

# Initialize a total vote counter
total_votes = 0

# Initialize a dictionary to hold the candidates and vote counts
candidate_votes = {}

# Path to the CSV file:
file_path = "Resources/election_data.csv"

# Read the CSV file 
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Count the total number of votes
        total_votes =   total_votes+ 1
       
        # Extract the candidate's name from each row
        candidate = row['Candidate']
       
        # If the candidate is already in the dictionary, increment their vote count by 1
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate]+ 1
        else:
            # If the candidate is not in the dictionary, add them and set their vote count to 1
            candidate_votes[candidate] = 1

#Print total Vote counts:
print("Election Results:")
print("----------------------------------")
print(f'\nTotal Votes: {total_votes}')
print("----------------------------------")

# Calculate the percentage of votes each candidate won and determine the winner
winner = None
max_votes = 0

for candidate, votes in candidate_votes.items():
    # Calculate the percentage of votes
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes} votes)')

    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the results: 
print("----------------------------------")
print(f'Winner: {winner} with {max_votes} votes')
print("----------------------------------")

#out_path= os.path.join("Pypoll","analysis","result.txt")
#with open (out_path,"w")as txt_file:
#    txt_file.write()

out_path = os.path.join("PyPoll", "analysis", "result.txt")
with open(out_path, "w") as txt_file:
    txt_file.write("Election Results:\n")
    txt_file.write("----------------------------------\n")
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write("----------------------------------\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f'{candidate}: {percentage:.3f}% ({votes} votes)\n')
    txt_file.write("----------------------------------\n")
    txt_file.write(f'Winner: {winner} with {max_votes} votes\n')
    txt_file.write("----------------------------------\n")
