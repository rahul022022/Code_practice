# WE can do this 
a = int(input("Enter Number A :- "))
b = int(input("Enter Number B :- "))
c = int(input("Enter Number C :- "))

if a<b and a<c:
    print(f"Value {a} is minmum")

elif b<a and b<c:
    print(f"Vlaue {b} is minimum")

else:
    print(f"Vlaue {c} is minimum")

# or we can use python in build min() function use.

a = int(input("Enter Number A :- "))
b = int(input("Enter Number B :- "))
c = int(input("Enter Number C :- "))

minimum = min(a,b,c)
print(F"This is minmum number out of this three {minimum} ")