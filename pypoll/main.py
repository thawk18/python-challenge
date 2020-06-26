# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("python-challenge","Resources","election_data.csv")

# Read the csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # use of next to skip first title row in csv file
    next(csvreader) 

    voter_id = [] #set as list 
    candidate = "" #set as string
    candidates = [] #set as list
    votes = {} #set as dictionary

    for row in csvreader:
        #transpose ids into line to count votes
        voter_id.append(int(row[0]))
        
        #Each Vote choice 
        candidate = row[2]
        
        #loop around and keep adding new candidate to new line
        if candidate not in candidates:
            candidates.append(candidate)
            
            #define dictionary and start counting
            votes[candidate] = 0
        else:
            #Meanwhile keep adding 1 vote each time the candidate is already in the list, keep dictionary
            votes[candidate] = votes[candidate] + 1
 
    #print headers
    print("Election Results")
    print("-------------------------------------")
    #print nr of voters
    print(f"Total Votes: {len(voter_id)}")
    print("-------------------------------------")
    #loop around to find candidate and total votes

for candidate in votes:
    total_votes = votes[candidate] + 1 # add 1 as first vote isn't included above!
    percentage = (total_votes/len(voter_id))*100 #just a simple division

    #write down candidates, % and total votes
    print(f"{candidate}: {percentage:.3f}% ({total_votes})")     

print("-------------------------------------")

namelist = list(votes.keys()) #set list of candidates from dictionary
votelist = list(votes.values()) #set list of results from dictionary

#print the winner gwtting the maximum value
print(f"Winner: {(namelist)[votelist.index(max(votelist))]}")
print("-------------------------------------")

# Specify the file to write to
output_path = os.path.join("output", "elections.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = "") as txtFile:

    # Write the first row
    txtFile.writelines("Election Results\n")
    # Write the second row
    txtFile.writelines("-------------------------------------\n")
    # And so on
    txtFile.writelines(f"Total Votes: {len(voter_id)}\n")
    txtFile.writelines("-------------------------------------\n")
    for each in votes: 
        candidate_name = each 
        total_votes = votes[each] + 1 
        percentage = (total_votes/len(voter_id))*100 
        txtFile.writelines(f"{candidate_name}: {percentage:.3f}% ({total_votes})\n")
    txtFile.writelines("-------------------------------------\n")
    txtFile.writelines(f"Winner: {(namelist)[votelist.index(max(votelist))]}\n")
    txtFile.writelines("-------------------------------------\n")
