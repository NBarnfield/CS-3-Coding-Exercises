# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except IOError:
    print("File name {} is not valid.".format(file))
    quit()

# Construct a dictionary
mbox_text = dict()

# Calculate the frequency of days the emails were sent
try:
    for line in fhand:
        if not line.startswith('From '): continue
        line = line.rstrip().split()
        word = line[2]
        mbox_text[word] = mbox_text.get(word, 0) + 1

except:
    print("There appears to be an error with {}. Please try again.".format(fhand))
    quit()

# Print results
if mbox_text == {}:
    print("Whoops, no luck! There were no lines that started with 'From '!!")
else:
    print(mbox_text)
