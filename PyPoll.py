# Adding the dependencies
import csv
import os
# Assign a variable to load a file from a path
election_results = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path
election_analysis = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open("Resources/election_results.csv") as election_data:
    # To do:read and analyze the data here
    # Read the file object with the reader function
    election_reader = csv.reader(election_data)   
# Print header row
    headers = next(election_reader)
    print(headers)
