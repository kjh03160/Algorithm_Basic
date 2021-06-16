# boj.kr/17951

def answer(L, max_v):
    global k
    left, right = 0, max_v

    while left <= right:
        mid = (left + right) // 2

        count = 0
        now = 0
        for i in range(n):
            now += L[i]
            if now >= mid:
                count += 1
                now = 0

        if count >= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
L = list(map(int, input().split()))
max_value = 0
for i in range(n):
    max_value += L[i]
print(answer(L, max_value))
