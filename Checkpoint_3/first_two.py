def ask_for_string():
    while True:
        user_input = input("Please enter an awesome alphabetic string or leave blank: ")
        if user_input.isalpha():
            return user_input
        elif not user_input:
            return user_input
        else:
            print("That is not valid input. Please enter an awesome alphabetic string or leave blank")


def first_two(string):
    if len(string) < 2:
        return string
    else:
        return string[:2]


def analyse_response(word, start_of_word):
    if len(word) == 0:
        print("You couldn't think of an awesome string! Maybe next time.")
    else:
        print("So your awesome string was '{}' and the beginning letters were {}!".format(word, start_of_word))


request_input = ask_for_string()
beginning_of_word = first_two(request_input)
analyse_response(request_input, beginning_of_word)


