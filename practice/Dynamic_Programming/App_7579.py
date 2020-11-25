# https://www.acmicpc.net/problem/7579

def answer(M, A, C):
    DP = [[0 for _ in range(100001)] for _ in range(len(A) + 1)]
    ans = []
    if len(A) == 1:
        return C[0]
    for app in range(len(A)):
        for co in range(10001):
            if C[app] > co:
                DP[app][co] = DP[app - 1][co]
            else:
                DP[app][co] = max(DP[app - 1][co], DP[app - 1][co - C[app]] + A[app])
            if DP[app][co] >= M:
                ans.append(co)
    return min(ans)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
apps = list(map(int, input().split()))
cost = list(map(int, input().split()))
print(answer(m, apps, cost))