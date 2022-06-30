# Adding the dependencies
import csv
import os
# Assign a variable to load a file from a path
election_results = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
election_analysis = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# candidate options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# winnng candidates and winning cont tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open("Resources/election_results.csv") as election_data:
   
    # To do:read and analyze the data here
    # Read the file object with the reader function
    election_reader = csv.reader(election_data)   
# Print header row
    headers = next(election_reader)

# Print each row in the csv file.
    for row in election_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print candidate name in each row.
        candidate_name = row[2]
        # if candidate does not mach any existing candidate
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

        #2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Save the results to our text file.
    with open(election_analysis, "w") as election_writer:
        election_results = (
            f"\nElection results\n"
            f"-------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        election_writer.write(election_results)
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes)/ float(total_votes) * 100
    # Print the candidate votes
            candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% of {votes:,}\n")
            print(candidate_results)
            election_writer.write(candidate_results)
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
            winning_candidate_summary = (f"----------------------------\n" 
            f"Winner : {winning_candidate}\n"   
            f"winning vote count: {winning_count:,}\n"
            f"winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------\n") 
        print(winning_candidate_summary)
        election_writer.write(winning_candidate_summary)