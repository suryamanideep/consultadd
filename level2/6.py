def check_two_power(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return check_two_power(n // 2)

n = int(input("Enter a number: "))
if check_two_power(n):
    print("True")
else:
    print("False")
