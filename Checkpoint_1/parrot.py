# Program name: parrot_trouble.py
# We have a loud talking parrot. The "hour" input is the current hour time
# in the range 0..23. We are in trouble if the parrot is talking
#(input True if talking and False if not) and the hour is before 7 or after 20.
#Return True if we are in trouble.
# Make sure all test cases below will pass.
# parrot_trouble(talking, hour)

def parrot_trouble(talking, hour):
    pass
    if talking == True:
        print("We could be in for some drama!")
    else:
        print("Quiet....perfect.")
    if hour > 7 or < 20:
        print("We are in trouble!")
    else:
        print("Thank goodness, a reasonable hour.")


hour = int(input("What is the hour? "))
talking = input("Is the parrot talking (y/n)? ")
