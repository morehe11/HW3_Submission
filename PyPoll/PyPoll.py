import os 
import csv 


dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)
#create path 
pypoll_path = os.path.join (dir_path, "Resources")
print(pypoll_path)
print(type(pypoll_path))
os.chdir(pypoll_path)

#empty lists 
candidate =[]
unique_candidate = []
percentages_per_candidate = []
candidate_vote_total = []
winner = []


#open and read file 
with open ("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
#next header
    next(csvreader)
   
#total votes among all candidates
    votesTotal = 0
    for row in csvreader:
        votesTotal += 1
        candidate.append(row[2])
#candidate specific data 
    for a in set (candidate):
    #add candidates to unique candidates lists only once
      unique_candidate.append(a)
    #how many votes each candidate received
      votes = candidate.count(a)
      candidate_vote_total.append(votes)
    #percentages of votes per candidate 
      percent = (votes/votesTotal)*100
      percentages_per_candidate.append(percent)

#use max to find winner 
winner_vote = max(candidate_vote_total)
winner_overall = unique_candidate[candidate_vote_total.index(winner_vote)]


print("Election Results")
print ("----------------")
print (f'Total Votes: {votesTotal}')
for i in range (len(unique_candidate)):
    print( f' {unique_candidate[i]}: {round(percentages_per_candidate[i], 2)}% ({candidate_vote_total[i]})')
print ("-----------------")
print (f' The winner is {winner_overall}')

#create write path to create new text file
pypoll_path_write = os.path.join(dir_path, 'analysis')
print(pypoll_path_write)
os.chdir(pypoll_path_write)

#open new file and write, \n to create new lines on the file 
with open ("pypoll_analysis.txt", "w") as text:
    text.write ("----------------\n" )
    text.write ("Election Results \n")
    text.write ("----------------- \n")
    text.write (f"Total Votes: {votesTotal}\n")
    text.write ("----------------- \n")
    for i in range (len(unique_candidate)):
        text.write( f"{unique_candidate[i]} : {round (percentages_per_candidate[i], 2)}% ({candidate_vote_total[i]}) \n" )
    text.write ("----------------- \n")
    text.write ( f"The winner is: {winner_overall} \n")
    text.write ("----------------- \n")






