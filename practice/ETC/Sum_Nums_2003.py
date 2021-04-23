# https://www.acmicpc.net/problem/2003
def answer(K):
    global m

    for i in range(len(K) - 1):
        K[i + 1] += K[i]
    start, end = 0, 1
    result = 0
    while start <= end:
        value = K[end] - K[start]
        if value < m:
            end += 1
        else:
            start += 1

        if value == m:
            result += 1

        if end == len(K):
            break

    return result

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
K = [0] + list(map(int, input().split()))
print(answer(K))