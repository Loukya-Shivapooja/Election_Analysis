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
* There were **369,711** votes cast in the election.
* The candidates were:
  * Candidate 1: Charles Casper Stockham
  * Candidate 2: Diana DeGette
  * Candidate 3: Raymon Anthony Doane
* The Candidate results were:
  * Candidate 1: Charles Casper Stockham received 23.0% of the vote and 85,213 number of the votes.
  * Candidate 2: Diana DeGette received 73.8% of the vote and 272,892 number of the votes.
  * Candidate 3: Raymon Anthony Doane received 3.1% of the vote and 11,606 number of the votes.
* The winner of the election was:
  * Candidate 2: **Diana DeGette** who received **73.8%** of the vote and 272,892 number of the votes.
## Overview of Election Audit:
### Purpose:
The purpose of this analysis is to collect additional data from the CSV file and submit to the election commission to complete the audit.
The data to be collected are:
* The voter turnout for each county.
* The percentage of votes from each county out of the total count.
* The county with the highest turnout.
### Election Audit Results
#### 1. Votes casted in the congressional election.
To count all the votes, we need to initialize a variable, which is called an **accumulator**, that will increment by 1 as we read each row in the `for` loop. For convenience, we will initialize a variable called `total_votes` to zero.

The `total_votes` variable needs to be placed above the code where we open the file, using the `with open()` statement. We do this because every time we run the file, the `total_votes` variable must be set equal to zero.

After we read the headers, we can iterate through each row and increment the `total_votes` variable by 1. To increment a variable is `number = number + 1`, which can be augmented to `number += 1`.

<img width="496" alt="Screen Shot 2022-07-03 at 2 52 46 PM" src="https://user-images.githubusercontent.com/107584361/177058480-a409b1a3-759e-4a55-842d-9a1906fdae28.png">.

#### 2. Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
When we add `county_turnout = 0`, we're setting each county's vote count to `zero`. Once we set it to `zero`, then we can start tallying the votes for each county.

To increment each county's vote count every time their name appears in a row, we need to move the vote counter inside the `for` loop and have it align with the `if` statement, the following code will illustrate in detail.

<img width="770" alt="Screen Shot 2022-07-03 at 3 05 37 PM" src="https://user-images.githubusercontent.com/107584361/177059069-df32a2fa-b194-4574-abeb-38da1dbac199.png">

#### 3. County with the largest number of votes.
we will create an `if` statement inside the `for` loop and do the following:
* Determine if the vote count that was calculated is greater than the `voter_count_turnout`.
* If the `voter_count` is greater than the `voter_count_turnout` and the percentage is greater than the voter_percentage, set the winning_count equal to the votes and set the winning_percentage equal to the vote_percentage.
* Set the winning_count equal to the variable, candidate_name, in the for loop.

<img width="762" alt="Screen Shot 2022-07-03 at 3 23 50 PM" src="https://user-images.githubusercontent.com/107584361/177059343-3b4623e6-5a19-4147-85d9-82859f1cbeb9.png">

#### 4. Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
To get the unique names in the candidate_options list, we can use an if statement with the not in membership operator to check if the candidate has been added to the list. If the candidate's name has been added to the list, then the next time the candidate's name is found in a row using the for loop, it will not be added to the list.

we will create an if statement inside the for loop and do the following:

* Determine if the vote count that was calculated is greater than the winning_count.
* If the vote count is greater than the winning_count and the percentage is greater than the winning_percentage, set the winning_count equal to the votes and set the winning_percentage equal to the vote_percentage.
* Set the winning_count equal to the variable, candidate_name, in the for loop.

The image below shows the code for calculating the number of votes and percentage each candidate received.

<img width="662" alt="Screen Shot 2022-07-03 at 3 41 43 PM" src="https://user-images.githubusercontent.com/107584361/177059829-731ccc2c-66eb-4164-a18b-0ebd84b574b0.png">

#### 5. Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
`If` statement checks the condition highest votes and percentage of each candidate and prints candidate with highest votes.

<img width="670" alt="Screen Shot 2022-07-03 at 3 52 50 PM" src="https://user-images.githubusercontent.com/107584361/177063697-ed4dec70-ad22-4689-bb10-c754be30292a.png">

We need to save the election results to a text file and then print the file to the screen to make sure that the results are in the correct format.

After the election analysis is written to the text file, the file should look like this:

<img width="484" alt="Screen Shot 2022-07-04 at 2 33 22 PM" src="https://user-images.githubusercontent.com/107584361/177218451-cee1c7b5-f925-4b0a-8572-4cdaf3af35af.png">

### Election Audit Summary:

This script can be used for any kind of election. We may need to make some small changes to allow the code to work with different data, but that should not be a problem.
* The first example of a different kind of election would be a very simple school election for choosing the student body president. This script can be modified by changing the county votes to student grade levels instead.
* The second example would be a nationwide presidential election. We could either change county to be state instead or we could add state in addition to county so we would have more detail.
