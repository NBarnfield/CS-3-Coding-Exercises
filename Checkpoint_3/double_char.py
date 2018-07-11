def ask_for_string():
    while True:
        user_input = input("Please enter an awesome alphabetic string or leave blank: ")
        if isinstance(user_input, str):
            return user_input
        elif not user_input:
            return user_input
        else:
            print("That is not valid input. Please enter an awesome alphabetic string or leave blank")


def double_char(given_string):
        doubled_letter = list()
        for letter in given_string:
            new_letter = letter + letter
            doubled_letter.append(new_letter)
        if len(doubled_letter) == 0:
            print("You entered a blank...no double characters for you!!!")
        else:
            print("".join(doubled_letter))


string = ask_for_string()
double_char(string)
