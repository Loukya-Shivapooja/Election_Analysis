# Election_Analysis
Election Analysis by Python
## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Detemine the winner of the election based on popular vote.

![images](https://user-images.githubusercontent.com/107584361/177018184-97c4ea2a-e322-4868-aee9-e6d249fc357e.jpeg)
## Resources
* Data Source : election_results.csv
* software : Python 3.6.1, Visual Studio Code 1.38.1.
## Summary
The analysis of the election show that:
* There were "369,711" votes cast in the election.
* The candidates were:
  * Candidate 1: Charles Casper Stockham
  * Candidate 2: Diana DeGette
  * Candidate 3: Raymon Anthony Doane
* The Candidate results were:
  * Candidate 1: Charles Casper Stockham received 23.0% of the vote and 85,213 number of the votes.
  * Candidate 2: Diana DeGette received 73.8% of the vote and 272,892 number of the votes.
  * Candidate 3: Raymon Anthony Doane received 3.1% of the vote and 11,606 number of the votes.
* The winner of the election was:
  * Candidate 2: Diana DeGette who received 73.8% of the vote and 272,892 number of the votes.
## Overview of Election Audit:
### Purpose:
The purpose of this analysis is to collect additional data from the CSV file and submit to the election commission to complete the audit.
The data to be collected are:
* The voter turnout for each county.
* The percentage of votes from each county out of the total count.
* The county with the highest turnout.
### Election Audit results
#### 1. Votes casted in the congressional election.
To determine the votes casted, first total votes are assigned to `zero` and is incremented.
<img width="496" alt="Screen Shot 2022-07-03 at 2 52 46 PM" src="https://user-images.githubusercontent.com/107584361/177058480-a409b1a3-759e-4a55-842d-9a1906fdae28.png">
#### 2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
A `for` loop is created to calculate the voters count in each county and the percentage of votes. 
<img width="770" alt="Screen Shot 2022-07-03 at 3 05 37 PM" src="https://user-images.githubusercontent.com/107584361/177059069-df32a2fa-b194-4574-abeb-38da1dbac199.png">
#### 3. County with the largest number of votes.
To Determine the county with largest number of votes, an `if` statement is used by checking the votes and percentage of each county and votes with highest county is printed.
<img width="762" alt="Screen Shot 2022-07-03 at 3 23 50 PM" src="https://user-images.githubusercontent.com/107584361/177059343-3b4623e6-5a19-4147-85d9-82859f1cbeb9.png">
#### 4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
the image below shows the code for calculating the number of votes and percentage each candidate received.
<img width="662" alt="Screen Shot 2022-07-03 at 3 41 43 PM" src="https://user-images.githubusercontent.com/107584361/177059829-731ccc2c-66eb-4164-a18b-0ebd84b574b0.png">
#### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
`If` statement checks the condition highest votes and percentage of each candidate and prints candidate wi
