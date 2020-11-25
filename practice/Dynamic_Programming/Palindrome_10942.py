# https://www.acmicpc.net/problem/10942


import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
m = int(input())
M = []
for _ in range(m):
    M.append(tuple(map(int, input().split())))

DP = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    x = 0
    for j in range(i, n):
        if x == j:
            DP[x][j] = True
        else:
            if x + 1 > j - 1:
                DP[x][j] = numbers[x] == numbers[j]
            else:
                DP[x][j] = DP[x + 1][j - 1] and numbers[x] == numbers[j]
        x += 1

# print(*DP, sep = '\n')
for k in M:
    print(1 if DP[k[0] - 1][k[1] - 1] else 0)