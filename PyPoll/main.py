#!/usr/bin/env python
# coding: utf-8

# In[173]:


#imports
import os
import csv
import pandas as pd
import numpy as np


# In[174]:


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


# In[175]:


#set directory
cwd = os.getcwd()
csvPath = os.path.join(cwd, 'Resources', 'election_data.csv')
df = pd.read_csv(csvPath)


# In[225]:


# opening and reading CSV module
with open(csvPath) as csvfile:

    # set delimiter
    csvreader = csv.reader(csvfile, delimiter = ',')

    #Converting headers of column to list
    pl_list = df['Voter ID'].tolist()
    county_list = df['County'].tolist()
    candidate_list = df['Candidate'].tolist()

    # set data type
    type(county_list)
    type(candidate_list)
    
    #Total votes in data
    sum_votes = len(df)

    # Adding all occurance of candidates

def summary():
    # Print information
    print(f"---------------------------------")
    print(f"ELECTION RESULTS")
    print(f"---------------------------------")
    print(f"Total Votes: {sum_votes}")
    print(f"---------------------------------")
    print(f"")
    print(f"")
    print(f"")
    print(f"")
    print(f"---------------------------------")
    print(f"Winner: ")
    print(f"---------------------------------")

summary()


# In[228]:


#output to .txt file
# def external(): 
#     with open('Financial_Analysis.txt', 'w') as f:
#         print(f"---------------------------------", file = f)
#         print(f"FINANCIAL ANALYSIS", file = f)
#         print(f"---------------------------------", file = f)
#         print(f"Total Months: {sum_month}", file = f)
#         print(f"Total Profit/Losses: ${sum_pl}", file = f)
#         print(f"Average Change in Profit/Losses: ${round(avg_change_pl, 2)}", file = f)
#         print(f"Greatest Increase in Profits: {maxincrease_day} (${maxincrease_pl})", file = f)
#         print(f"Greatest Decrease in Profits: {minincrease_day} (${minincrease_pl})", file = f)
#         print(f"---------------------------------", file = f)
# external()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




