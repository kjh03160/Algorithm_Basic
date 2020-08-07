def selection_sort(arr, n):
    for i in range(n):
        x = i
        for j in range(i + 1, n):   # arr[i + 1] 부터 arr[n - 1] 중 최솟값 인덱스 찾기
            if arr[x] > arr[j]:
                x = j
        arr[i], arr[x] = arr[x], arr[i]     # swap


