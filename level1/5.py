num = int(input("enter a number for factorial: "))
prod = 1
for i in range(1,num+1):
    prod*=i
print(f"factorial of the given number {num} is {prod}")