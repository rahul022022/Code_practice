choice = input("Convert to (F)ahrenheit or (C)elsius? Enter F or C: ")

if choice.upper() == "F":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

elif choice.upper() == "C":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F = {celsius}°C")

else:
    print("Invalid choice! Please enter F or C.")
