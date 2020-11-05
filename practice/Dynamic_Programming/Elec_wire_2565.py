# https://www.acmicpc.net/problem/2565

def answer(L):
    L.sort()
    DP = [1] * len(L)
    for point in range(len(L)):
        for j in range(point):
            if L[point][1] > L[j][1]:
                DP[point] = max(DP[point], DP[j] + 1)
    return len(L) - max(DP)

import sys
input = sys.stdin.readline
n = int(input())
L = []

for _ in range(n):
    L.append(tuple(map(int, input().split())))

print(answer(L))