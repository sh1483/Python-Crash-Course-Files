def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
# while True:
#    print("\nPlease tell me your name:")
#    f_name = input("First name: ")
#    l_name = input("Last name: ")


# formatted_name = get_formatted_name(f_name, l_name)
# print(f"\nHello, {formatted_name}!")

# Here we use a condition to quit the loop.
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' a any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break


    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
