#import dependencies
import os
import csv

#join file paths
path1 = os.path.join(".", "raw_data", "election_data_1.csv")
path2 = os.path.join(".", "raw_data", "election_data_2.csv")

#initiate values and lists
voter_num = 0
candidates_list = []
candidates_votes = []
candidates_votes_percentage = []

#define function
def get_results(path):

    #make variable global to use both inside of function
    global voter_num
    global candidate_list
    global candidates_votes
    global candidates_votes_percentage

    #open file
    with open(path, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)

        #loop through rows
        for row in reader:
            voter_num += 1
            current_candidate = row["Candidate"]
            
            #add unique candidates and votes to lists
            if current_candidate not in candidates_list:
                candidates_list.append(current_candidate)
                candidates_votes.append(0)
                candidates_votes_percentage.append(0)
                index = candidates_list.index(current_candidate)
                candidates_votes[index] += 1
            else:
                index = candidates_list.index(current_candidate)
                candidates_votes[index] += 1

#use function on two files
get_results(path2)

#get total votes
total_votes = sum(candidates_votes)

#calculate vote percentage for candidates
for i in range(len(candidates_list)):
    candidates_votes_percentage[i] = candidates_votes[i] / float(total_votes)

#calculate max vote percentage for candidates
max_candidates_votes_percentage = max(candidates_votes_percentage)
max_candidates_votes_percentage_index = candidates_votes_percentage.index(max_candidates_votes_percentage)
winner = candidates_list[max_candidates_votes_percentage_index]

#save the candidates data in report as a string:
candidates_string = ""
for i in range(len(candidates_list)):
    current_candidate_string = candidates_list[i] + ": " + "{:.2%}".format(candidates_votes_percentage[i]) + "% (" + str(candidates_votes[i]) + ")\n"
    candidates_string = candidates_string + current_candidate_string

#save the report as a string:
report_string = "```\n" + "Election Results\n" + "-------------------------\n"\
+ f"Total Votes: {total_votes}\n" + "-------------------------\n"\
+ candidates_string + "-------------------------\n"\
+ f"Winner: {winner}\n" + "-------------------------\n" + "```\n"

#create a report function
def report():
    print(report_string)

#print report
report()

#save report to txt
output_file = os.path.join("output.txt")
with open(output_file, "w") as f:
    f.write(report_string)