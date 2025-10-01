num1 = 5
num2= 10

# Numerical comparisons
print(f"{num1} == {num2} is {num1 == num2}")
print(f"{num1} != {num2} is {num1 != num2}")
print(f"{num1} < {num2} is {num1 < num2}")
print(f"{num1} > {num2} is {num1 > num2}")
print(f"{num1} <= {num2} is {num1 <= num2}")
print(f"{num1} >= {num2} is {num1 >= num2}")



name1 = "Alice"
name2 = "Bob"
print(f"{name1} is {name1 == name2}")
print(f"{name1} is {name1 < name2}")

age = 25
voting_age = 18

print("Can this person vote?")
print(f"Age: {age}, Voting age: {voting_age}")
if(age >= voting_age):
    print("This person can vote")
else:
    print("This person cannot vote")


age2 = 18
if age2 >= 18:
    print("You can vote")
print("This will always print")

person_age = -75

if person_age >0 and person_age <13:
    print("Child ticket: $5")
elif person_age >= 13 and person_age < 65:
    print("Adult ticket: $12")
elif person_age > 65:
    print("Senior ticket: $8")
else:
    print("Invalid input")

    
