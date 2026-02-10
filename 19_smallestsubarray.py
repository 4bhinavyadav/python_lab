def smallest_subarray(arr, x):
    n = len(arr)
    current_sum = 0
    left = 0
    min_length = n+1

    for right in range(n):
        current_sum += arr[right]

        while current_sum > x:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    if min_length <= n:
        return min_length
    else:
        return 0 

print(smallest_subarray([1, 5, 10], 11))

