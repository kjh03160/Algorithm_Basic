# https://www.acmicpc.net/problem/2751

def quicksort(l, start, end):
    if start >= end:
        return
    x = partition(l, start, end)
    quicksort(l, start, x - 1)
    quicksort(l, x + 1, end)

def partition(l, start, end):
    pivot = l[end]
    index = start
    div = start

    while index < end:
        if l[index] < pivot:
            l[index], l[div] = l[div], l[index]
            div += 1
        index += 1

    l[div], l[index] = l[index], l[div]
    return div

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

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left = merge_sort(arr[0:m])
    right = merge_sort(arr[m:])
    return merge(left, right)

def merge(left,right):
    sort = []
    i = 0; j = 0
    while (i < len(left) and j < len(right)):
        if left[i] > right[j]:
            sort.append(right[j])
            j += 1
        else:
            sort.append(left[i])
            i += 1

    if i == len(left):
        sort = sort + right[j:]
    if j == len(right):
        sort = sort + left[i:]

    return sort


def answer(l):
    return merge_sort(l)


import sys

input = sys.stdin.readline

n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

l = answer(l)
for _ in l:
    print(_)