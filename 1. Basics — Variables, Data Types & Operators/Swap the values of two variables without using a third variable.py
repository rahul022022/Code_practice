# This both without third variable
a = 20
b = 10

print("Before Swap Value A:",a)
print("Before Swap Value B:",b)
a,b=b,a

print("After Swap Value A:",a)
print("After Swap Value B:",b)


a = 22
b = 10 
c = 44

print("Before swaping values :",a,b,c)

a,b,c = c,b,a

print("After swaping values :",a,b,c)

a = 88
b = 100
print("before swap:",a,b)
c = b,a
print("After value swap",a,b)

# This is with third variable

a = 10
b = 20

print("Before swap :",a,b)

temp = a
a = b
b = temp

print("After swap :",a,b)