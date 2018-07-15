import csv
import os
from collections import Counter

electionData = os.path.join("Resources" , "election_data.csv") 
with open(electionData, newline='') as csvfile:
    electionResults = csv.reader(csvfile, delimiter=',')
    next(electionResults,None)

    voterid = []
    county = []
    candidates = []
    
    for row in electionResults:
        voterid.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

    canSet = set(candidates)    
    totalVote = len(voterid)
    cnt = Counter(candidates)
    canNames = []
    
    for row in canSet:  
        canNames.append(row)

    print("Election Results")
    print("----------------------------------------")
    print(f"The total number of votes was {totalVote}")
    print("----------------------------------------")
    f = open("Output_analysis.txt" , "w")
    f.write("Election Results"+ "\n")
    f.write("-------------------------------------"+ "\n")
    f.write("Total Votes : "+ str({totalVote}) + "\n")
    f.write("-------------------------------------"+ "\n")
    dictOfCan = {}
    candidateCount = 0
    for row in canNames:
        candidateName = str(canNames[candidateCount])
        votes = candidates.count(candidateName)
        votes = int(votes)
        percentage = round(votes / totalVote * 100, 2)
        dictOfCan.update({ candidateName : votes})
        #.sort_values(by = "Voter ID", ascending=False)
        print(f"{candidateName}: {percentage}%  ({votes})" )
        f.write(f"{candidateName}: {percentage}%  ({votes})" + "\n")
        candidateCount = candidateCount + 1

    import operator

    winner = max(dictOfCan, key=lambda key: dictOfCan[key])
    print("----------------------------------------")
    print("Winner: ", winner)    
    print("----------------------------------------")
    f.write("-------------------------------------" + "\n")
    f.write("Winner : "+ winner + "\n")
    f.write("-------------------------------------"+ "\n")
    f.close()

