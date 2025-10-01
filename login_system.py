# Set a correct username and password in your program
# Ask the user for their credentials
# Check if BOTH username AND password are correct
# Give appropriate messages for different scenarios:
# Both correct: "Welcome!"
# Wrong username only: "Username not found"
# Wrong password only: "Incorrect password"
# Both wrong: "Invalid credentials"

# Set the correct credentials
correct_username = "admin"
correct_password = "secret123"


username = input("User Name:\n")
password = input("Password:\n")

if username == correct_username and (password == correct_password):
    print("Welcome")
elif (username != correct_username) and (password == correct_password):
    print("User name not found")
elif (username == correct_username) and (password != correct_password):
    print("Incorrect password")
else:
    print("Invalid credentials")


