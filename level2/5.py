def temperature_info(arr):
    arr.sort()
    avg_temp = sum(arr)/len(arr)
    return arr[0],arr[-1],avg_temp

arr = [int(i) for i in input("enter the temprature: ").split(",")]
lowest_temp,highest_temp,avg_temp = temperature_info(arr)
print(f" Average Temperature: {avg_temp}\n Highest Temperature: {highest_temp}\n Lowest Temperature: {lowest_temp}")