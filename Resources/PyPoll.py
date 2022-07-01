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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers= next(file_reader)

    print(headers)
    print("Hello")
    
