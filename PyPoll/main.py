#########################################
# Analyzing Poll Data                   #
#########################################

import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join("", "Resources","election_data.csv")

# Path to export the result to text file
pypoll_txt = os.path.join("Analysis", "pypoll_analysis.txt")

# Set list of candidates
candidates = []

# Set list of distinct candidates
distinct_candidates = []

# Set list of votes count per candidates
votes_per_candidates = []

# Set list of votes percentage per candidates
percent_per_candidates = []

# Set list of votes count total per candidates
candidate_vote_list = []

# Read the csv file
with open(pypoll_csv, newline="")as csvfile:

    # Split the data on commas
    pypoll_csv = csv.reader(csvfile,delimiter=",")

    # Get the first row and store in header to skip and go to next row
    header = next(pypoll_csv)

    # Initialize the row counter to 0
    voterCounter = 0


     # Loop through the data in pypoll_csv row by row
    for data in pypoll_csv:

        # Add 1 to voterCounter to move to next row
        voterCounter+=1

        # Add candidate name to candidates list
        candidates.append(data[2])


#print("Election Results")
#print("-----------------------------")
#print("Total Votes : " + str(voterCounter))
#print("-----------------------------")

output = ( f"Election Results\n"
           f"-----------------------------\n"
           f"Total Votes : {voterCounter}\n"
           f"-----------------------------\n")
          
# Export the results to text file
with open(pypoll_txt, "w") as txt_file:
    txt_file.write(output)

print(output)
# create list of distinct candidates by looping through each row 
for x in candidates:
    if x not in distinct_candidates:
        distinct_candidates.append(x)

        # count votes per candidates
        votes_per_candidates = candidates.count((distinct_candidates[-1]))

        # calculate percentage votes per candidates
        percent_per_candidates = format(((votes_per_candidates/voterCounter)*100), '.3f')

        # append candidate vote list per candidate
        candidate_vote_list.append(int(votes_per_candidates))
        
        # get the maximum vote
        max_vote = max(candidate_vote_list)

        # get the index of maximum vote from the list
        max_vote_index = candidate_vote_list.index(max_vote)

        # get the name of candidate who gets the maximum vote with the same index of maximum vote
        candidate_name_winner = distinct_candidates[max_vote_index]
        
 ######## print distinct candidate name with percentage count and total vote count
        output2=(((distinct_candidates[-1]) + " : " + (str(percent_per_candidates)) + "% "+ "(" + (str(votes_per_candidates)) + ")\n"))
        print(output2)

        # Append-adds at last
        with open(pypoll_txt, "a") as txt_file:  
            txt_file.write(output2)



output3 = ( f"-----------------------------\n"
            f"Winner : {candidate_name_winner}\n"
            f"-----------------------------\n")

print(output3)

# Append-adds at last
with open(pypoll_txt, "a") as txt_file:  
    txt_file.write(output3)



