# Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead
# of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents
# of your dictionary.

# Ask user for file name input.
file = input("Enter file: ")

# Attempt to open the file, otherwise quit on failure.
try:
    fhand = open(file, 'r')
except ValueError:
    print("File name {} is not valid.".format(file))
    quit()

# Construct a dictionary
mbox_emails = dict()

# Calculate the number of emails that were sent by each email address
try:
    for line in fhand:
        if not line.startswith('From '): continue
        line = line.translate(line.maketrans('@', ' '))
        line = line.rstrip().split()
        email = line[2]
        mbox_emails[email] = mbox_emails.get(email, 0) + 1

except ValueError:
    print("There appears to be an error with {}. Please try again.".format(fhand))
    quit()


# Use a maximum loop to determine which email sent the most emails.
largest_email = None

for email in mbox_emails:
    if largest_email is None or mbox_emails[email] > largest_email:
        largest_email = mbox_emails[email]
        sender = email

# Print results
if mbox_emails == {}:
    print("Whoops, no luck! There were no lines that started with 'From '!!")
else:
    print(mbox_emails)
    print("The most emails were sent from {} with a total of {} emails.".format(sender, largest_email))
