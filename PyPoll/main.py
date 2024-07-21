import csv

# Initialize a total vote counter
total_votes = 0

# Initialize a dictionary to hold the candidates and vote counts
candidate_votes = {}

# Path to the CSV file:
file_path = "PyPoll/election_data.csv"

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

