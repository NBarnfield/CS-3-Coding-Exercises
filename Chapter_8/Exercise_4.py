# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except:
    print("File name {} is not valid.".format(file))
    quit()

# Create a list to append each word in the text to.
shakespeare_list = []

# For each line, clean any whitespace away and then add it to the list if it is a unique entry.
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word in shakespeare_list:
            continue
        else:
            shakespeare_list.append(word)

# Print the list to double check the output is correct.
print(shakespeare_list)