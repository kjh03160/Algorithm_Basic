# https://www.acmicpc.net/problem/12865

def answer(w, L):
    DP = [[0] * (w + 1) for _ in range(len(L) + 1)]

    for i in range(1, len(L) + 1):
        for j in range(1,  w + 1):
        # for j in range(L[i - 1][0], 1) 은 만약 해당 무게가 w 값을 벗어나면 0으로 채워지기에
        # 이전 값과 비교할 때, 0과 비교를 하게 되어 잘못된 값을 넣게 된다.
            if j >= L[i - 1][0]:
                DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - L[i - 1][0]] + L[i - 1][1])
            else:
                DP[i][j] = DP[i - 1][j]
    return DP[len(L)][w]

import sys
input = sys.stdin.readline
n, w = map(int, input().split())
things = []
for _ in range(n):
    things.append(tuple(map(int, input().split())))

print(answer(w, things))