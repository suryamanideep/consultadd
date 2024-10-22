str_arr = [i for i in input().split(",")]
for i in range(len(str_arr)):
    temp = []
    for j in str_arr[i]:
        temp.append(j)
    #print(temp)
    str_arr[i] = temp
print(str_arr)