# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("python-challenge","Resources","budget_data.csv")

# Read the csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # use of next to skip first title row in csv file
    next(csvreader) 
    
    #define new lines of values
    total = []
    month = []
    difference = []

    # loop to count and sum rows, transpose into lines to do operations... 
    # this is not panda! 
    for row in csvreader:
        #transpose values to line
        total.append(int(row[1]))
        #transpose months to line
        month.append(row[0])

    #loop around months values next to each other (remember total is now a line)
    for i in range(1,len(total)): 
        difference.append(total[i] - total[i-1]) #get new line values with all differences
        
        #average is just a sum of these differences divided by number of months
        average_difference = float(sum(difference)/(len(month)-1)) #(and removing first month as it doesn't have a previous month)

        #finding max & min differences (difference variable is still a line so let's use a formula)
        max_difference = max(difference)
        min_difference = min(difference)

        #months were transposed to line but is offset by 1 as difference only starts on second month
        #range above started at 1 and not 0 so difference is delayed
        #we need to add 1 to the index and catch the train
        max_difference_month = (month[difference.index(max_difference)+1])
        min_difference_month = (month[difference.index(min_difference)+1])

    #print all values found
    print("Financial Analysis") #print headers
    print("-------------------------------------") 
    print(f"Total Months: {len(month)}")  #print with count of months
    print(f"Total: ${sum(total)}") #print with sum of total
    print(f"Average Change: ${average_difference:.2f}")
    print(f"Greatest Increase in Profits: {max_difference_month} (${max_difference})")
    print(f"Greatest Decrease in Profits: {min_difference_month} (${min_difference})")

# Specify the file to write to
output_path = os.path.join("output", "financial_analysis.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline = "") as txtFile:

    # Write the first row
    txtFile.writelines("Financial Analysis\n")
    # Write the second row
    txtFile.writelines("-------------------------------------\n")
    # And so on
    txtFile.writelines(f"Total Months: {len(month)}\n")
    txtFile.writelines(f"Total: ${sum(total)}\n")
    txtFile.writelines(f"Average Change: ${average_difference:.2f}\n")
    txtFile.writelines(f"Greatest Increase in Profits: {max_difference_month} (${max_difference})\n")
    txtFile.writelines(f"Greatest Decrease in Profits: {min_difference_month} (${min_difference})\n")
