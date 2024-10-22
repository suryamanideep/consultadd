nums = [int(i) for i in input("enter the number Range").split()]
nums.sort()
print(nums)
sum_odd =0
for i in range(nums[0],nums[1]):
    if i%2 == 1:
        sum_odd+=i
print(f"sum of odd numbers: {sum_odd}")