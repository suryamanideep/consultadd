a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
[len , len2] = [a,b] if len(a) > len(b) else [b,a]
for i in len:
    if i in len2:
        print(i,end=",")