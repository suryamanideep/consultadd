def count_pairs_with_sum(arr, N, K):
    count = 0
    freq_map = {}

    for i in range(N):
        complement = K - arr[i]
        if complement in freq_map:
            count += freq_map[complement]
        if arr[i] in freq_map:
            freq_map[arr[i]] += 1
        else:
            freq_map[arr[i]] = 1

    return count
arr = [int(i) for i in input("enter Array: ").split(",")]
N = len(arr)
K = 6

print(count_pairs_with_sum(arr, N, K))
