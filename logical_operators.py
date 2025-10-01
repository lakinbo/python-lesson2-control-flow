is_sunny = True
is_warm = True
has_time = False

if is_sunny and is_warm:
    print("Perfect beach day!")
if is_sunny and is_warm and has_time:
    print("Let's go to the beach")
else:
    print("Maybe another time")

is_raining = True
is_cold = True
is_Tired = False

if is_raining or is_cold:
    print("Perfect beach day!")
if is_raining or is_cold or is_Tired:
    print("Good day to stay at home")

is_weekend = False
is_busy = True
    
if not is_weekend:
    print("It's a weekday")
if not is_busy:
    print("Free to hang out!")

# Truth Table
print("Truth Table for AND")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

print("Truth Table for OR")
print(f"True or True = {True and True}")
print(f"True or False = {True and False}")
print(f"False or True = {False and True}")
print(f"False or False = {False and False}")

