# #The data we need to retrieve
# #1. The total number of votes cast
# #2. A complete list of candidates who received votes
# #3. The percentage of votes each candidate won
# #4. The total number of votes each candidate won
# #5. The winner of the election based on popular vote

# # # Import the datetime class from the datetime module.
# # import datetime as dt

# # # Use the now() attribute on the datetime class to get the present time.
# # now = dt.datetime.now()

# # #Print the present time.
# # print("The time now is", now)

# #import dependencies
# #import csv library
# import csv

# #allows us to access files indirectly
# import os 

# # #Direct file access
# # # Assign a variable for the file to load and the path.
# # file_to_load ='C:/Users/15619/Bootcamp/my_work/Module 3/Election_Analysis/Resources/election_results.csv'

# # # Open the election results and read the file
# # with open(file_to_load) as election_data:

# #      # To do: perform analysis.
# #      print(election_data)

# # Assign a variable for the file to load and the path.
# # To declare a variable for the file to load, connect the os.path submodule with the join() function
# file_to_load = os.path.join("election_results.csv")

# # Open the election results and read the file
# with open(file_to_load) as election_data:

#     # Print the file object.
#     print(election_data)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("..","analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write three counties to the file.
#      txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

# # Close the file
# txt_file.close()

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("..", "analysis", "election_analysis.txt")

#initiate an accumulator (counter) for total votes
total_votes = 0

#make list for candidate names
candidate_options = []

#make a dictionary for number of voters for each candidate
candidate_votes = {}

#variables for winning candidate
winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row, also excluding it from data read.
    headers= next(file_reader)

    #print(headers)

    #add total votes by iterating through each row in csv file
    for row in file_reader:

        #add to the total vote count
        total_votes += 1

        #candidate name is in the third column
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
       
            #print the candidate name 
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
        
#Save the results to the text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (f"Election Results\n"
        f"----------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------\n")
    print(election_results, end = "")

    #save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    #Iterate through the candidate list.
    for candidate_name in candidate_options:
        
        #Retrieve vote count of a candidate. Be sure to put votes on the left to name the variable
        votes = candidate_votes[candidate_name]

        #Calculate the percentage of votes.
        percentage_votes = (float(votes)/float(total_votes)) * 100 

        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate_name}: {percentage_votes:.1f}%({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (percentage_votes > winning_percentage):
            
            #If true then set winning_count = votes and winning_percent vote_percentage.
            winning_count = votes
            winning_percentage = percentage_votes

            #Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_statement = (f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    print(winning_candidate_statement)

    #save winning candidate results to text file
    txt_file.write(winning_candidate_statement)
