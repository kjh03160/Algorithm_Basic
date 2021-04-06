# boj.kr/2294

def answer(L, k):
    DP = [float('inf') for _ in range(k + 1)]
    for i in range(1, k + 1):
        for coin in L:
            if coin > i:
                continue
            if i % coin == 0:
                DP[i] = min(i // coin, DP[i])
            else:
                DP[i] = min(DP[i], DP[i - coin] + 1)
    return DP[-1]

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
L = set()
for _ in range(n):
    x = int(input())
    L.add(x)
result = answer(L, k)
print(result if result != float('inf') else -1)