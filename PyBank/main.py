#!/usr/bin/env python
# coding: utf-8

# In[3]:


#imports
import os
import csv
import pandas as pd
import numpy as np


# In[4]:


# * In this challenge, you are tasked with creating a Python script for
# analyzing the financial records of your company. You will give a set of
# financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
# The dataset is composed of two columns: `Date` and `Profit/Losses`.
# (Thankfully, your company has rather lax standards for accounting so the
# records are simple.) * Your task is to create a Python script that analyzes
# the records to calculate each of the following:
#   * The total number of months included in the dataset
#   * The net total amount of "Profit/Losses" over the entire period
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
# * As an example, your analysis should look similar to the one below:
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
# * In addition, your final script should both print the analysis to the
	# terminal and export a text file with the results.
#


# In[5]:


#set directory
cwd = os.getcwd()
csvPath = os.path.join(cwd, 'Resources', 'budget_data.csv')
df = pd.read_csv(csvPath)


# In[10]:


# opening and reading CSV module
with open(csvPath) as csvfile:

    # set delimiter
    csvreader = csv.reader(csvfile, delimiter = ',')

#   Converting 'Date' and Profit/Losses' column to a list
    pl_list = df['Profit/Losses'].tolist()
    day_list = df['Date'].tolist()
    
#   Total months in data
    sum_month = len(day_list)

#   Sum of profit/losses
    sum_pl = sum(pl_list)

#   Average change in profit/losses
    numpy_diff_list = np.diff(pl_list)
    diff_list = numpy_diff_list.tolist() # Change diff_list from NumPy to a regular list
    sum_diff_list = sum(diff_list)
    avg_change_pl = float(sum_diff_list/(len(diff_list)))

#   Greatest Increase in Profits:
    maxincrease_diff = max(diff_list)
    maxincrease_index = diff_list.index(maxincrease_diff)
    maxincrease_raw = maxincrease_index + 1
    maxincrease_day = day_list[maxincrease_raw]
    maxincrease_pl = pl_list[maxincrease_raw]

#   Greatest Decrase in Profits:
    minincrease_diff = min(diff_list)
    minincrease_index = diff_list.index(minincrease_diff)
    minincrease_raw = minincrease_index + 1
    minincrease_day = day_list[minincrease_raw]
    minincrease_pl = pl_list[minincrease_raw]

def summary():
    # Print information
    print(f"---------------------------------")
    print(f"FINANCIAL ANALYSIS")
    print(f"---------------------------------")
    print(f"Total Months: {sum_month}")
    print(f"Total Profit/Losses: ${sum_pl}")
    print(f"Average Change in Profit/Losses: ${round(avg_change_pl, 2)}")
    print(f"Greatest Increase in Profits: {maxincrease_day} (${maxincrease_pl})")
    print(f"Greatest Decrease in Profits: {minincrease_day} (${minincrease_pl})")
    print(f"---------------------------------")

summary()


# In[16]:


#output to .txt file
txtpath = os.path.join("analysis", "analysis.txt")

def external(): 
    with open(txtpath, 'w') as f:
        print(f"---------------------------------", file = f)
        print(f"FINANCIAL ANALYSIS", file = f)
        print(f"---------------------------------", file = f)
        print(f"Total Months: {sum_month}", file = f)
        print(f"Total Profit/Losses: ${sum_pl}", file = f)
        print(f"Average Change in Profit/Losses: ${round(avg_change_pl, 2)}", file = f)
        print(f"Greatest Increase in Profits: {maxincrease_day} (${maxincrease_pl})", file = f)
        print(f"Greatest Decrease in Profits: {minincrease_day} (${minincrease_pl})", file = f)
        print(f"---------------------------------", file = f)
external()


# In[14]:


maxincrease_index


# In[ ]:





# In[ ]:





# In[ ]:




