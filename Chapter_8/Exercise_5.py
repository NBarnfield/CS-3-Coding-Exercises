# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except:
    print("File name {} is not valid.".format(file))
    quit()

# Set a counter to count how many lines started with 'From '.
counter = 0

# Loop through the text. If the line doesn't begin with 'From ' continue, otherwise split, print and count.
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):continue
    text_list = line.split()
    print(text_list[1])
    counter = counter + 1

# Print how many lines began with 'From '.
print("There were {} lines in this text that began with From as the first word.".format(counter))