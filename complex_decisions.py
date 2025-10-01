# score = int(input("Enter your test score:\n"))

# if score >=90 and score <100:
#     print(f"Grade: A - Excellent")
# elif score >=80 and score <90:
#     print("Grade: B - Good job!")
# elif score >=70 and score <80:
#     print("Grade: C - Satisfactory")
# elif score >=60 and score <70:
#     print("Grade: D - Needs Improvement")
# elif score >=0 and score <60:
#     print("Grade: F - See me!")
# else: print("Invalid input...nice try!")

light_color = input("What color is the traffic light?").lower()
if light_color == "green":
    print("Go!")
elif light_color == "yellow":
    print("Caution - Prepare to Stop")
elif light_color == "red":
    print("Stop!")
else: 
    print("Invalid Input")

