import os
#Read the election data from the csv file

#Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

total_votes=0
candidate_names=[] 
percentage_votes=0
total_votes=0
winner=[]
candidate_votes={}

# print(cvspath)
with open(csvpath) as csvfile:

    #CVS reader specifies delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')

 # print(csvreader)

  #Read the header row first
    csv_header=next(csvreader)
 # print(f"CSV Header: {csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        #print(row)
        total_votes = total_votes+1
        current_candidate_name = row[2]
             
          
            
        if current_candidate_name not in candidate_names:
            candidate_names.append(current_candidate_name)
            candidate_votes[current_candidate_name] = 0
        candidate_votes [current_candidate_name]= candidate_votes[current_candidate_name]+1

        
        
        
        
print("Election Results")
print("-------------------------")
print("Total Votes:" + " " +str(total_votes))
print("-------------------------")
print(candidate_names)


