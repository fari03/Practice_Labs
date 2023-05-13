import re

password = input("Enter your password: ")

# Check if password meets all the criteria
if len(password) < 6 or len(password) > 16:
    print("Password must be between 6 and 16 characters.")
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
elif not re.search("[0-9]", password):
    print("Password must contain at least one digit.")
elif not re.search("[$#@]", password):
    print("Password must contain at least one of the following special characters: $, #, @")
else:
    print("Password is valid.")
