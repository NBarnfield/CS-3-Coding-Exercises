"""The program below reads a dataset containing reviews of Donna Tartt’s The Goldfinch in the Amazon book review.
These reviews have been stored in a simple tab separated file, which is nothing more than a plain text file with
columns. The table contains four columns: review score, url, review title and review text.

Your task is to put comments on each line explaining what it does. First few lines are already commented for you.
You can put a copy of the code in your GitHub account with the comments in it. Thanks.  """


# Import required library
import urllib.request

# Load the data from remote location (URL)
file = urllib.request.urlopen(
    "https://gist.githubusercontent.com/twielfaert/a0972bf366d9aaf6cb1206c16bf93731/raw/dde46ad1fa41f442971726f34ad03aaac85f5414/Donna-Tartt-The-Goldfinch.csv")

f = file.read()

# Transform the bitstream into strings
text = f.decode(encoding='utf-8', errors='ignore')

# Split text into lines by line breaks
lines = text.split("\n")

# Create a dictionary to count the number of ratings per rating score and counter variable
counts = dict()
counter = 0

# For each line split based on a tab
for line in lines:
    l = line.strip().split("\t")

    # Assign list values to a variable
    score = l[0]
    id = l[1]
    title = l[2]
    review = l[3]

    # If score is unique add it to the counts dict, otherwise add + 1 to its value. Increase counter by 1.
    counts[score] = counts.get(score, 0) + 1
    counter = counter + 1

# Convert the counter variable to a string and print. Print a string of the number of lines in the text.
print(str(counter))
print(str(len(lines)))

# Print out each key and value in the counts dictionary.
for key, val in counts.items():
    print(key, val)
