# https://www.acmicpc.net/problem/4963
# 문제점 : 재귀 호출 스택 초과 -> pypy3 는 통과됨
def island(index):
    global ans
    G = graphs[index]
    visited = visits[index]

    def DFS(row, col):
        visited[row][col] = True

        for dir in direction:
            next_row, next_col = row + dir[0], col + dir[1]
            if 0 <= next_row < len(G) and 0 <= next_col < len(G[row]):
                if not visited[next_row][next_col] and G[next_row][next_col] == 1:
                    G[next_row][next_col] = 0
                    DFS(next_row, next_col)

    for row in range(len(G)):
        for col in range(len(G[row])):
            if G[row][col] == 1:
                ans += 1
                DFS(row, col)
    return ans

import sys
sys.setrecursionlimit()
direction = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]   # 오른쪽 위, 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래
graphs = []
visits = []
ans = 0

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    G = []
    for i in range(h):
        G.append(list(map(int, input().split())))
    visits.append([[False for _ in range(w)] for __ in range(h) ])
    graphs.append(G)

for i in range(len(graphs)):
    ans = 0
    print(island(i))