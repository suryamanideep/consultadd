import math
number1 = int(input("enter a number: "))
number2 = int(input("enter a number: "))
LCM = abs(number1*number2)//math.gcd(number1,number2)
print(f"LCM of {number1} and {number2} are: {LCM}")