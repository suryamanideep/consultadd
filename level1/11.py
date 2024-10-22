digit_sum = int(input())
while digit_sum >= 10:
    digit_sum = sum(int(digit) for digit in str(digit_sum))
    print(f"Again compute the sum of digits so that it can be reduced to one single digit: {digit_sum}")

print("Final Output:", digit_sum)