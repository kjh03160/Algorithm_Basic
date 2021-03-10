# https://www.acmicpc.net/problem/2467
def answer(K):
    i, j = 0, len(K) - 1
    result = float('inf')
    x, y = None, None
    while i < j:
        a, b = K[i], K[j]
        dif = a + b

        if abs(dif) < result:
            result = abs(dif)
            x, y = a, b

        if dif < 0:
            i += 1
        elif dif > 0:
            j -= 1
        else:
            break
    return x, y

import sys
input = sys.stdin.readline
n = int(input())
K = list(map(int, input().split()))
print(*answer(K))