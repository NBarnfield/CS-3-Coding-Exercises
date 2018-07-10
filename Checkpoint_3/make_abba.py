def ask_for_string():
    while True:
        user_input = input("Please enter an awesome alphabetic string: ")
        if user_input.isalpha():
            return user_input
        else:
            print("That is not valid input. Please enter an awesome alphabetic string")


def make_abba(string_a, string_b):
    print(string_a + string_b + string_b + string_a)


first_string = ask_for_string()
second_string = ask_for_string()
make_abba(first_string, second_string)
