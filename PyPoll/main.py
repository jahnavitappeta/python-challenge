import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    voter_count = 0
    candidates = {}

#computing votes per candidate.
    for row in csvreader:
        voter_count += 1
        candidates[row[2]] = candidates.get(row[2], 0) + 1

    fileContent = str(f'Election Results\n')
    fileContent += str(f'-------------------------\n')
    fileContent += str(f'Total votes: {voter_count}\n')
    fileContent += str(f'-------------------------\n')
    for k,v in candidates.items():
        percent_voter = v/voter_count * 100
        fileContent += str(f'{k}: {percent_voter:.3f}% ({v})\n')
        #fileContent += str('{0}: {1:.3f}% ({2})\n'.format(k,percent_voter,v))
    
    fileContent += str(f'-------------------------\n')
    winner = max(candidates,key=candidates.get)
    fileContent += str(f'Winner: {winner}\n')
    fileContent += str(f'-------------------------')
    
    print(fileContent)
    file = open('Output.txt','w')
    file.write(fileContent)
    file.close()