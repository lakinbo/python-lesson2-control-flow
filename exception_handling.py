# try:
#     age = int(input("Enter your age: "))
#     print(f"You are {age} years old")
# except ValueError:
#     print("Invalid input")

# print("Execution continues...")

try:
    num1 = int(input("Enter first number:\n"))
    num2 = int(input("Enter second number:\n"))
    result = num1/num2
    print(f"{num1}/{num2} = {result}")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Please enter valid numbers")
except Exception as e:
    print(f"An error has occurred! {e}")
