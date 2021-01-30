# https://www.acmicpc.net/problem/11051

def answer(n, k):
    DP = [[0], [1, 1], [1, 2, 1]]
    for i in range(2, n):
        temp = [1]
        for x in range(len(DP[i]) - 1):
            temp.append(sum(DP[i][x: x + 2]) % 10007)
        temp.append(1)
        DP.append(temp)
    return DP[n][k] % 10007


import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(answer(n, k))