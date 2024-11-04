#Write a Python function called greet_friends
# that can take an arbitrary number of friend names as arguments.
# The function should print a greeting for each friend
# in the format: "Hello, [friend_name]!".
# If no names are provided,
# the function should print: "No friends to greet."
# Call the function with the names "Alice", "Bob", and "Charlie".

def great_function(*friends):
    if not friends:
        print("no friend to great.")
    else:
        for friend in friends:
            print(f"hello, {friend}!")

great_function("alice","bob","charlie")

