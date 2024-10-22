arr = [int(i)for i in input("enter Array: ").split(",")]
i = 0
try:
    for i in range(len(arr)+1):
        arr[i]+=i
except IndexError:
    print(f"Error: Index {i} is out of range. The list has only {len(arr)} elements.")