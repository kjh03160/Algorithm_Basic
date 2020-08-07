def insertion_sort(arr, n):     # arr[0] ~ arr[n-1]까지
    for i in range(1, n):
        j = i - 1
        while arr[j] > arr[j + 1] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
