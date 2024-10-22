def rotate_right(arr, D):
    N = len(arr)
    D = D % N
    rotated_array = arr[N-D:] + arr[:N-D]
    return rotated_array
arr = [int(i) for i in input().split(",")]
D = 2

rotated_arr = rotate_right(arr, D)
print(rotated_arr)
