# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def quicksort(arr, first, last):
    if first >= last:
        return
    x = partition(arr, first, last)
    quicksort(arr, first, x - 1)
    quicksort(arr, x + 1, last)

def partition(arr, first, last):
    pivot = arr[last]   # 피벗 설정
    i = first  # 탐색 위치
    b = first  # Big 그룹 시작 위치
    while i < last: # last 까지 탐색하기
        if arr[i] < pivot:  # 피벗보다 작은 값 찾음
            swap_elements(arr, b, i)    # Big 그룹 시작 직전의 값과 현재 값(pivot보다 작은)을 swap
            b += 1  # Big 그룹의 인덱스 + 1
        i += 1  # 탐색 위치 + 1

    swap_elements(arr, b, i)    # 피벗이 들어갈 위치로 swap
    return b    # 피벗의 위치 리턴

# not in place
def quicksort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    L, M, R = [], [], []
    for i in arr:
        if i < pivot:
            L.append(i)
        elif i > pivot:
            R.append(i)
        else:
            M.append(i)
    return quicksort2(L) + M + quicksort2(R)
