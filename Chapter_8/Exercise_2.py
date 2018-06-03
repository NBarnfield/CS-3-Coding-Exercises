# Exercise 2: Figure out which line of the above program is still not properly guarded. See if you can construct a
# text file which causes the program to fail and then modify the program so that the line is properly guarded and test
# it to make sure it handles your new text file.


def clean_words(list_it)?????

fhand = open('ruin_code.txt')
count = 0
for line in fhand:
    words = line.split()
    #TODO: Remove special characters so that variations will be accepted.words = [words.replace((":", "") for word in words]
    print('Debug:', words)
    if len(words) == 0 : continue
    words[0].capitalize()
    if words[0] != 'From' : continue
    print(words[2])
