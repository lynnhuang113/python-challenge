import os
import csv

election_data = "election_data.csv"

candidate_votes = []
candidate_List = []
votes = -1
winner_votes = 0
total_candidates = 0
greatest_votes = [" ", 0]
Khan = 0
Correy = 0
Li= 0
Otooley = 0
with open(election_data, 'r') as csvfile:
          csvreader = csv.reader(csvfile,delimiter=',')
          header = next(csvreader)

          for row in csvreader: 
                    votes = votes + 1
                    candidate_List.append(row[2])
          candidate_List.pop(0)

          for i in candidate_List:
                    if i == "Khan":
                              Khan += 1
                    elif i == "Correy":
                              Correy+= 1
                    elif i == "Li":
                              Li+= 1
                    else:
                              Otooley += 1
winner_votes = max(Khan,Correy,Li,Otooley)
candidates = ["Khan","Correy","Li","Otooley"]
total_per_candidates = [Khan, Correy, Li, Otooley]
new_list = list(zip(candidates,total_per_candidates))
   
winner = 0
for j in new_list:
          if winner_votes == j[1]:
            winner = j[0]
            
analysis = "Election Results" + '\n' + '-' * 100 + '\n' +\
"Total Votes: " + str(votes) + '\n' + '-' * 100 + '\n' +\
"Khan: " + str(round(Khan/votes * 100, 2)) +'% (' + str(Khan) + ')' + '\n'+\
"Correy: " + str(round(Correy/votes * 100,2)) + '% (' + str(Correy) + ')' + '\n' +\
"Li: " + str(round(Li/votes * 100,2)) + '% (' + str(Li) + ')' + '\n' +\
"O'Tooley: " + str(round(Otooley /votes * 100,2)) + '% ('+str(Otooley) + ')' + '\n' + '-' * 100+ '\n' +\
"Winner: " + winner
print(analysis)

with open(os.path.join(os.path.dirname(__file__),"pypoll.txt"), "w") as file:
        file.write(analysis)
