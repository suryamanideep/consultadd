nums = [int(i) for i in input().split(", ")]
hashmap = {}
for i in nums:
    if i in hashmap:
        hashmap[i]+=1
    else:
        hashmap[i] = 1
print(hashmap)