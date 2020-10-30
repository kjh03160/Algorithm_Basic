# https://www.acmicpc.net/problem/1427

import math
def answer(n):
    digit = int(math.log10(n))
    num_list = []
    for i in range(digit + 1):
        x = (n // (10 ** i)) % 10
        num_list.append(x)

    def merge_sort(list_1, start, end):
        if start >= end:
            return

        mid = (start + end) // 2
        merge_sort(list_1, start, mid)
        merge_sort(list_1, mid + 1, end)

        result = []

        left = start
        right = mid + 1

        while left <= mid and right <= end:
            if num_list[left] <= num_list[right]:
                result.append(num_list[right])
                right += 1
            else:
                result.append(num_list[left])
                left += 1
        for _ in range(left, mid + 1):
            result.append(num_list[_])
        for _ in range(right, end + 1):
            result.append(num_list[_])

        for k in range(start, end + 1):
            num_list[k] = result[k - start]

    merge_sort(num_list, 0, len(num_list) - 1)

    return num_list


import sys
input = sys.stdin.readline

n = int(input())
print(*answer(n), sep='')