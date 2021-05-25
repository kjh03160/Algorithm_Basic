# boj.kr/9024

def answer(L, k):
    results = []
    diff = float('inf')
    L.sort()

    start, end = 0, len(L) - 1
    while start < end:
        x = L[start] + L[end] - k

        if diff == abs(x):
            results.append((L[start], L[end]))
        elif diff > abs(x):
            results.clear()
            results.append((L[start], L[end]))
            diff = abs(x)

        if x < 0:
            start += 1
        elif x == 0:
            start += 1
            end -= 1
        else:
            end -= 1
    return results

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    L = list(map(int, input().split()))
    print(len(answer(L, k)))