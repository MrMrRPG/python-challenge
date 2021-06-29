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
# --------------------------------------------------------------------------------------------------------------------------

import os
import csv
import pandas as pd
import numpy as np

# set directory
cwd = os.getcwd()
# print (cwd)
csvPath = os.path.join(cwd, 'Resources', 'budget_data.csv')
df = pd.read_csv(csvPath)

# opening and reading CSV module
with open(csvPath) as csvfile:

	# set delimiter
	csvreader = csv.reader(csvfile, delimiter = ',')
		
	sum_month = len(df)
	net_total_pl = df.sum(axis = 1, skipna = True)
	avg_pl = net_total_pl/sum_month

	# Print information
	print(f"Fiancial Analysis")
	print(f"---------------------------------")
	print(f"Total Months: {sum_month}")
	print(f"Total: ${net_total_pl}")
	print(f"Average Change: ${avg_pl}")
	# print(f"Greatest Increase in Profits: $ {maxincrease_profits}")
	# print(f"Greatest Decrease in Profits: $ {minincrease_profits}")
	# print(f"---------------------------------")

	# # print(csvreader)
	# print out header
	# csv_header = next(csvreader)
	# print(f"csv header: {csv_header}")

	# # print out df data
	# for df in csvreader:
	# 	print(df)

# # Definitions
# def print_analysis(summary):

# 	# Assigning column variable
# 	date = str(summary[0])
# 	pl = int(summary[1])

# 	# sum_month = len(df)
# 	# net_total_pl = 0
# 	# avg_pl = 0
# 	maxincrease_date = ""
# 	minincrease_date = ""
# 	maxincrease_profits = 0
# 	minincrease_profits = 0

