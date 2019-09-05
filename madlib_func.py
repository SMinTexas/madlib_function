# Write a function that accepts two arguments: a name and a subject.
# The function should return a String with a name and subject interpolated in.
# For example:
#
# madlib("Jen", "science") # "Jenn's favorite subject is science."
# madlib("Jeff", "history") # "Jeff's favorite subject is history."
#
# Provide default arguments in case one or both are omitted.

def madlib(name, subject):
    if name == "":
        name = "Darth Vader"

    if subject == "":
        subject = "Planetary Demolition"

    print(f'{name}\'s favorite subject is {subject}.')

continue_to_run = True

while continue_to_run == True:
    input_name = input("What is your name? ")
    input_subject = input("What is your favorite subject? ")

    madlib(input_name, input_subject)

    choice = input("Enter Y to continue, or N to Exit ")
    if choice == "N":
        continue_to_run = False