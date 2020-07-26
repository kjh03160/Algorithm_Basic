def merge(list1, list2):
    i = 0
    j = 0
    new_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    if i < len(list1):
        new_list += list1[i:]
    if j < len(list2):
        new_list += list2[j:]
    # new_list += list1[i:] + list2[j:]
    return new_list

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    return merge(merge_sort(my_list[:mid]), merge_sort(my_list[mid:]))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
