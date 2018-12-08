##Importing modules. os module allows us to create file paths and csv modules allows us to read csv files.
import os
import csv

#Specify file path
cvfilepath = os.path.join("election_data.csv")

#Read csv
with open(cvfilepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Read header
    csvheader=next(csvreader)

    #Create 3 empty lists to hold values in each column of csv file
    voters = []
    counties = []
    candidates = []
    
    #Looping through the csv
    for row in csvreader:

        #Append values in above lists
        voters.append(int(row[0]))
        counties.append(row[1])
        candidates.append(row[2])
  
    #Create an empty list to store unique candidates
    unique_candidates = []
    
    #Loop through candidate list to identify unique candidates
    for x in candidates:
        if x not in unique_candidates:
            unique_candidates.append(x)
    
    #Initialize a list to hold total vote count and percentage for each candidate
    vote_count_list = []
    vote_percent_list = []

    #Count the occurrence of each candidate in the candidates list to get total votes for each candidate
    for c in unique_candidates:
        #Calculate total votes
        candidate_votes = candidates.count(c)
        
        #Caculate vote percentage
        vote_percent = round(100*(candidate_votes/len(candidates)),2)

        #Append both values to their respective lists
        vote_count_list.append(candidate_votes)
        vote_percent_list.append(vote_percent)
    
    #Now we have three lists - unique_candidates,vote_count_list,vote_percent_list

    #Find winner with highest no. of votes
    highest_votes = max(vote_count_list)
    index_of_higest_votes = vote_count_list.index(highest_votes)
    candidate_with_highest_votes=unique_candidates[index_of_higest_votes]
    
    #START DISPLAYING ALL RESULTS
    
    print('Election Results')
    print('------------------------')
    
    #Display total votes by counting no. of voters
    print(f'Total Votes: {len(voters)}')
    print('------------------------')
    
    #Initialize summary table to use for the output file
    summary_list=[]

    for y in unique_candidates:
        z= y + ' ' + str(vote_percent_list[unique_candidates.index(y)]) + '% ('+ str(vote_count_list[unique_candidates.index(y)]) + ')'
        #print(f'{y}: {vote_percent_list[unique_candidates.index(y)]}% ({vote_count_list[unique_candidates.index(y)]})')
        summary_list.append(z)
        print(z)

    #Display winner
    print('------------------------')
    print(f'Winner: {candidate_with_highest_votes}')
    print('------------------------')
    
    
    #Redirect output of all print statements to a text file
    with open('PyPoll_output.txt', 'w') as f:
        f.write('Election Results' '\n'
            '------------------------' '\n'
            f'Total Votes: {len(voters)}' '\n'
            '------------------------' '\n'
            f'{summary_list[0]}' '\n'
            f'{summary_list[1]}' '\n'
            f'{summary_list[2]}' '\n'
            f'{summary_list[3]}' '\n'
            '------------------------' '\n'
            f'Winner: {candidate_with_highest_votes}' '\n'
            '------------------------')