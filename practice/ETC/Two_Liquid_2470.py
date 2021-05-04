# boj.kr/2470

def answer(L):
    L.sort()
    start, end = 0, len(L) - 1

    min_v = float('inf')
    a, b = 0, 0
    while start < end:
        value = L[end] + L[start]

        if abs(value) < min_v:
            a, b = start, end
            min_v = abs(value)

        if value > 0:
            end -= 1
        elif value < 0:
            start += 1
        else:
            a, b = start, end
            return L[a], L[b]
    return L[a], L[b]


import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
print(*answer(L))