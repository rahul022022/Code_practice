num1 = int(input("Enter Number 1 ->"))
num2 = int(input("Enter Number 2 ->"))
num3 = int(input("Enter Number 3 ->"))

if num1>num2:
    if num1>num3:
        print(f"{num1} is Max")
    else:
        print(f"{num3} is Max")

elif num2>num3:
    print(f"{num2} is Max")

else:
    print(f"{num3} is Max")

    
