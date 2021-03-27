# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


import sys

input = sys.stdin.readline
n, T = input().split()
n = int(n)
T = T.split(":")
T = int(T[0]) * 60 * 60 + int(T[1]) * 60 + int(T[2])
L = [0]

for _ in range(n):
    h, m = input().split(":")
    time = int(h) * 60 + int(m)
    time = L[-1] + time
    L.append(time)

def answer(n, T, L):
    start = 0
    end = start + 1
    max_count = 1
    result = start, end
    while True:
        sum_time = L[end] - L[start]
        if sum_time < T:
            end += 1
        else:
            if max_count < end - start:
                max_count = end - start
                result = start, end
            start += 1

        if end >= n:
            break

    return result

result =answer(n, T, L)
print(result[-1] - result[0], result[0] + 1)
