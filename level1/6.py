def is_perfect_number(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n
number = int(input("Enter a number: "))
if is_perfect_number(number):
    print("Yes")
else:
    print("No")