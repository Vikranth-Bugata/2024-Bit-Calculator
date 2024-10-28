# ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):
    error = "Please enter an number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
for item in range(0, 2):
    integer = int_check("integer: ", 1)
    print(integer)

print()

for item in range(0, 2):
    height = int_check("height: ", 1)
    print(height)
