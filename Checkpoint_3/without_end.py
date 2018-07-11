def ask_for_string():
    while True:
        user_input = input("Please enter an awesome alphabetic string with at least 2 characters: ")
        if len(user_input) > 2 and isinstance(user_input, str):
            return user_input
        else:
            print("That is not valid input. Please enter an awesome alphabetic string.")


string = ask_for_string()
new_string = string[1:-1]
print("This is the string you wrote {} and the middle of the word is {}".format(string, new_string))
