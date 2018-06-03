# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except:
    print("File name {} is not valid.".format(file))
    quit()

# Create a dictionary
flat_land_text = dict()

# Strip each of the lines and feed it into the dictionary
for line in fhand:
    line = line.rstrip()
    text_list = line.split()
    for word in text_list:
        flat_land_text[word] = flat_land_text.get(word, 0) + 1

print(flat_land_text)