import os 
import csv 

dir_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(dir_path)

pypoll_path = os.path.join (dir_path, "Resources")
print(pypoll_path)
print(type(pypoll_path))
os.chdir(pypoll_path)

candidate =[]

with open ("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    print(csvreader)

    next(csvreader)

    votesTotal = 0

    for row in csvreader:
        votesTotal += 1
        if str(row [2]) != str(row[2]):

            candidate.append (row[2])

        

print(votesTotal)
print(candidate)


#total # of votes cast


#complete list of candidates


#total numbers for each candidate

#winner based on popular vote 

