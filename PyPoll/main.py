#!/usr/bin/env python
# coding: utf-8

# In[105]:


#imports
import os
import csv
import pandas as pd
import numpy as np


# In[106]:


# * In this challenge, you are tasked with helping a small, rural town modernize
# its vote counting process.
# * You will be give a set of poll data called
# [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is
# composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is
# to create a Python script that analyzes the votes and calculates each of the
# following: * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.
# * As an example, your analysis should look similar to the one below:
#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
# * In addition, your final script should both print the analysis to the
# terminal and export a text file with the results.


# In[107]:


#set directory
cwd = os.getcwd()
csvPath = os.path.join(cwd, 'Resources', 'election_data.csv')
df = pd.read_csv(csvPath)


# In[ ]:





# In[129]:


#Setting some variables
candidates = []
candidatevote = []

# opening and reading CSV module
with open(csvPath) as csvfile:

    # set delimiter
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Converting headers of column to list
    pl_list = df['Voter ID'].tolist()
    county_list = df['County'].tolist()
    candidate_list = df['Candidate'].tolist()
    
    #Total votes in data
    sum_votes = len(df)
    
    #Looping through each row in raw data:
    for row in csvreader:
        name = row[2]
        
        if(name not in candidates):
            candidates.append(name)
            candidatevote.append(1)
        else:
            position = candidates.index(name)
            candidatevote[position] += 1
            
    # Candidate Vote Percentage
    vote_ratio_np = np.divide(candidatevote, sum_votes)
    vote_ratio = vote_ratio_np.tolist()
    
    #finding the winner using index
    winner_count_np = max(vote_ratio)
    winner_index = vote_ratio.index(winner_count_np)

def summary():
    # Print information
    print(f"---------------------------------")
    print(f"ELECTION RESULTS")
    print(f"---------------------------------")
    print(f"Total Votes: {sum_votes}")
    print(f"---------------------------------")
    
    for candidate_index in range(len(candidates)):
        if candidate_index == 0:
            continue
        else:
            vote_ratio_fr = float(vote_ratio[candidate_index])
            candidate_name = str(candidates[candidate_index])
            votes = int(candidatevote[candidate_index])
    
        print(f"{candidate_name}: {vote_ratio_fr:.3%} ({votes})")
    
    print(f"---------------------------------")
    print(f"Winner: {candidates[winner_index]}")
    print(f"---------------------------------")

summary()


# In[131]:


# output to .txt file
txtpath = os.path.join("analysis","analysis.txt")

def external(): 
    with open(txtpath, 'w') as f:
        print(f"---------------------------------", file = f)
        print(f"ELECTION RESULTS", file = f)
        print(f"---------------------------------", file = f)
        print(f"Total Votes: {sum_votes}", file = f)
        print(f"---------------------------------", file = f)

        for candidate_index in range(len(candidates)):
            if candidate_index == 0:
                continue
            else:
                vote_ratio_fr = float(vote_ratio[candidate_index])
                candidate_name = str(candidates[candidate_index])
                votes = int(candidatevote[candidate_index])

            print(f"{candidate_name}: {vote_ratio_fr:.3%} ({votes})", file = f)

        print(f"---------------------------------", file = f)
        print(f"Winner: {candidates[winner_index]}", file = f)
        print(f"---------------------------------", file = f)
external()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




