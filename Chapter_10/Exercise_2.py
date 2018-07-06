# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except ValueError:
    print("{} is not a valid file.".format(file))
    quit()

# Construct a dictionary
mbox_emails = dict()

# Calculate the number of emails that were sent by each email address and add them to the dictionary
try:
    for line in fhand:
        if not line.startswith('From '): continue
        line = line.translate(line.maketrans(':', ' '))
        line = line.rstrip().split()
        email_hour = line[5]
        mbox_emails[email_hour] = mbox_emails.get(email_hour, 0) + 1

except ValueError:
    print("There appears to be an error with {}. Please ensure there is a line that begins with 'From '.".format(fhand))
    quit()

# Construct a list to sort the dictionary
t = list()

for key, value in mbox_emails.items():
    t.append((value, key))

t.sort(reverse=True)

# Print top email sender
for value, key in t[:10]:
    print(key, value)
