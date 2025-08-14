P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest (%): "))
T = float(input("Enter time (in years): "))

SI = (P * R * T) / 100
CI = P * ((1 + R/100) ** T) - P

print(f"Simple Interest = {SI}")
print(f"Compound Interest = {CI}")
