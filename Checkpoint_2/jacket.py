def weather(temp):
    if temp < 20:
        print("That's chilly! Make sure you take your heavy jacket today!")
    elif temp < 30:
        print("What a lovely temperature! Take your bright light jacket in case there is a slight wind!")
    else:
        print("That's hot!!! Don't worry about bringing a jacket - but maybe take a hat!")


# Ask user for the temperature
while True:
    try:
        temperature = float(input("What is the temperature today? "))
        break
    except ValueError:
        print("That's not an integer or float! Try again!")

# Pass it in as an argument to the weather function
weather(temperature)