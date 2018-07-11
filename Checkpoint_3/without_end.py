def ask_for_string():
    while True:
        user_input = input("Please enter an awesome alphabetic string with at least 2 characters: ")
        if len(user_input) > 2 and isinstance(user_input, str):
            altered_input = user_input[1:-1]
            return user_input, altered_input
        else:
            print("That is not valid input. Please enter an awesome alphabetic string.")


# Store multiple return values into variables and print
string, altered_string = ask_for_string()
print("This is the string you wrote {} and the middle of the word is {}".format(string, altered_string))

