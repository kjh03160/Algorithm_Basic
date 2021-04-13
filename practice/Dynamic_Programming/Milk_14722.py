# boj.kr/14722
def answer(G):
    DP = [[[0, 0, 0] for j in range(len(G[0]))] for i in range(len(G))]
    next_milk = {0: 1, 1: 2, 2: 0}
    now_milk = 0
    DP[0][0][0] = 1
    # print(*DP, sep='\n')
    # 0 -> 1 -> 2
    for i in range(len(G)):
        for j in range(len(G[0])):
            now = G[i][j]
            if now == 0:
                # 이전 가게까지 2번 우유 마셨을 때의 최대 개수
                DP[i][j][0] = max(DP[i][j - 1][2] + 1, DP[i - 1][j][2] + 1)
            else:
                # 현재 1번 우유를 마실 수 없다면
                DP[i][j][0] = max(DP[i][j - 1][0], DP[i - 1][j][0])

            # 0번을 먹지 않은 상태에서 1번을 마실 수 있는 경우을 회피하기 위해
            if now == 1 and DP[i][j][2] < DP[i][j][0]:
                DP[i][j][1] = max(DP[i][j - 1][0] + 1, DP[i - 1][j][0] + 1)
            else:
                DP[i][j][1] = max(DP[i][j - 1][1], DP[i - 1][j][1])

            if now == 2 and DP[i][j][0] < DP[i][j][1]:
                DP[i][j][2] = max(DP[i][j - 1][1] + 1, DP[i - 1][j][1] + 1)
            else:
                DP[i][j][2] = max(DP[i][j - 1][2], DP[i - 1][j][2])

    return max(DP[-1][-1])


import sys
input = sys.stdin.readline
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
print(answer(G))