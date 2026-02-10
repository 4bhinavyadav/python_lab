def min_chocolate_difference(arr, m):
    if m == 0 or len(arr) < m:
        return -1

    arr.sort()
    min_diff = float('inf')

    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff

print(min_chocolate_difference([3, 4, 1, 9, 56, 7, 9, 12], 5))