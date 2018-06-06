# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except:
    print("File name {} is not valid.".format(file))
    quit()

# Create a dictionary
mbox_text = dict()

# Strip each of the lines and feed it into the dictionary
for line in fhand:
    if not line.startswith('From '): continue
    line = line.rstrip()
    text_list = line.split()
    mbox_text[word] = text_list[2] #.get(word, 0) + 1

print(mbox_text)