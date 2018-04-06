# This is a small example from Python for Everybody demonstating how an if else multi-way decision works

x = float(input("What number would you like to test the size of?"))

if x < 2:
    print("Small")
elif x < 10 :
    print("Medium")
else :
    print("Large!")

print("All done!")

# All decisions will be tested with the program exiting the if statement with the first correct test.
# This means that all code will be tested sequentially with only one path executed.