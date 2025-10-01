# Ask the user for temperature in Celsius
# Give appropriate clothing advice based on the temperature:
# Below 0°C: "Wear a heavy coat!"
# 0-10°C: "Wear a warm jacket!"
# 11-20°C: "A light jacket is fine"
# Above 20°C: "T-shirt weather!"

temperature = float(input("What's the temperature in Celsius?\n"))
if temperature <0:
    print("Wear a heavy coat")
elif temperature <=10:
    print("Wear a warm jacket!")
elif temperature<=20:
    print("A light jacket is fine")
else:
    print("T-shirt weather")


