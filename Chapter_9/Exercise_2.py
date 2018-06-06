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
    print(text_list)
    for word in text_list:
        mbox_text[word] = mbox_text.get(text_list[2], 0) + 1

print(mbox_text)