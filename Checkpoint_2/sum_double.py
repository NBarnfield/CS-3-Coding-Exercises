#5. Program name: sum_double.py
#Given two int values, return their sum. Unless the two values are the same, then return double their sum
#sum_double(first number, second number)


# Create a function to accept two integers, and either add and multiply if they are equal, or just add them together.
def sum_double(x, y):
    "Add two integers if they are different, or add them and multiply them if they are equal"
    if x == y:
        doubled = ((x + y) * 2)
        print("{} and {} are equal...let's add them together and double them! That equals {}".format(x, y, doubled))
        # If requiring a return value.
        #return doubled
    else:
        added = x + y
        print("Let's add {} and {} together! That equals {}".format(x, y, added))
        # If requiring a return value.
        #return added

# Using the function, compute the following.
print("Let's do some maths!")
sum_double(1, 2)
sum_double(3, 2)
sum_double(2, 2)
sum_double(-1, 0)
sum_double(3, 3)
sum_double(0, 0)
sum_double(0, 1)
sum_double(3, 4)
print("All done!")
