#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Candidate_list = []

with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for i in csvreader:
        
        # The total number of votes cast
        total_votes = total_votes + 1    
        
        # A complete list of candidates who received votes
        Candidate = i[2]
        if Candidate not in Candidate_list:
            Candidate_list.append(Candidate)

        # The total number of votes each candidate won
        x = Candidate
        if x == "Khan":
            Khan_votes = Khan_votes + 1
        if x == "Correy":
            Correy_votes = Correy_votes + 1
        if x == "Li":
            Li_votes = Li_votes + 1
        if x == "O'Tooley":
            OTooley_votes = OTooley_votes + 1

        # The percentage of votes each candidate won
        K_percent = Khan_votes/total_votes
        C_percent = Correy_votes/total_votes 
        L_percent = Li_votes/total_votes
        O_percent = OTooley_votes/total_votes

# The winner of the election based on popular vote
results_list = [C_percent, K_percent, L_percent, O_percent]
Candidate_list = sorted(Candidate_list)
win_votes = max(results_list)
winner = Candidate_list[results_list.index(win_votes)]

# Export

print("Election Results")
print("---------------------")
print("Total Votes:", total_votes)
print("---------------------")
print("Khan:", '{:.3%}'.format(K_percent), Khan_votes)
print("Correy:", '{:.3%}'.format(C_percent), Correy_votes)
print("Li:", '{:.3%}'.format(L_percent), Li_votes)
print("O'Tooley:", '{:.3%}'.format(O_percent), OTooley_votes)
print("---------------------")
print("Winner:", winner) 


# In[ ]:




