# boj.kr/2473

def answer(L):
    L.sort()
    a, b, c = 0, 0, 0

    min_v = float('inf')
    for i in range(len(L) - 2):
        start, end = i + 1, len(L) - 1

        while start < end:
            value = L[end] + L[start] + L[i]

            if abs(value) < min_v:
                min_v = abs(value)
                a, b, c = i, start, end

            if value > 0:
                end -= 1
            elif value < 0:
                start += 1
            else:
                return L[i], L[start], L[end]

    return L[a], L[b], L[c]


import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
print(*answer(L))