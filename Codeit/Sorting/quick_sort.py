# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    pivot = my_list[end]
    i = start  # 피벗보다 큰 수가 끝나는 위치
    b = start  # 피벗보다 큰 수가 시작되는 위치
    while i < end:
        if my_list[i] < pivot:
            swap_elements(my_list, b, i)
            b += 1
        i += 1

    swap_elements(my_list, b, i)
    return b

# 퀵 정렬
def quicksort(my_list, start, end):
    if start >= end:
        return
    q = partition(my_list, start, end)
    quicksort(my_list, start, q - 1)
    quicksort(my_list, q + 1, end)


def quicksort2(my_list, start=0, end=None):
    if end is None:
        end = len(my_list) - 1
    if start >= end:
        return
    q = partition(my_list, start, end)
    quicksort(my_list, start, q - 1)
    quicksort(my_list, q + 1, end)



# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)


# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort2(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort2(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort2(list3) # start, end 파라미터 없이 호출
print(list3)