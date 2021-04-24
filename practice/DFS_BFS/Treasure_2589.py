# boj.kr/2589

from collections import deque
def answer(G):
    direction = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    max_t = 0

    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == "L":
                visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
                q = deque()
                q.append((i, j, 0))
                visited[i][j] = True
                while q:
                    r, c, t = q.popleft()

                    max_t = max(max_t, t)

                    for row, col in direction:
                        drow, dcol = r + row, c + col
                        if 0 <= drow < len(G) and 0 <= dcol < len(G[0]) and not visited[drow][dcol] and G[drow][dcol] == "L":
                            visited[drow][dcol] = True
                            q.append((drow, dcol, t + 1))
    return max_t


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = [input().rstrip() for _ in range(n)]
print(answer(G))