import string

# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except ValueError:
    print("{} is not a valid file.".format(file))
    quit()

# Construct a dictionary
letters_dictionary = dict()

# For each line in the text strip them of digits and punctuation, split them, break into words and calculate letters
try:
    for line in fhand:
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.translate(line.maketrans('', '', string.digits))
        line = line.lower().rstrip().split()
        for word in line:
            word_tuple = tuple(word)
            for letter in word_tuple:
                letters_dictionary[letter] = letters_dictionary.get(letter, 0) + 1

except ValueError:
    print("There appears to be an error with {}.".format(fhand))
    quit()

# Construct a list to sort the dictionary
t = list()

for key, value in letters_dictionary.items():
    t.append((value, key))

t.sort(reverse=True)

# Print top 10 letters
for value, key in t[:10]:
    print(key, value)
