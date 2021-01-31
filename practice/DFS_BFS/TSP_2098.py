# https://www.acmicpc.net/problem/2098


def answer(visited, cur):
    global DP, G, n
    visited = visited | (1 << cur)  # 현재 마을 방문 표

    if visited == 2 ** n - 1:  # 모든 마을 방문 완료
        if G[cur][0] != 0:  # 현재 마을에서 시작한 마을 0번으로 돌아갈 경로가 있는지
            return G[cur][0]  # 있다면 돌아갈때의 가중치 반
        else:
            return float('inf')

    if DP[visited][cur] != float('inf'):    # 이미 방문했던 도시일 때
        return DP[visited][cur]

    for 마을 in range(n):
        if (visited >> 마을) % 2 == 0 and G[cur][마을] != 0:
            # 방문하지 않은 마을이고, 현재 마을에서 해당 마을로 갈 수 있을 때
            DP[visited][cur] = min(answer(visited, 마을) + G[cur][마을], DP[visited][cur])  # 더 짧 거리가 있을 경우 업데이트

    return DP[visited][cur]


import sys

input = sys.stdin.readline
n = int(input())
G = []

for _ in range(n):
    G.append(list(map(int, input().split())))

DP = [[float('inf') for _ in range(n)] for _ in range(2 ** n)]
print(answer(0, 0))
