# https://www.acmicpc.net/problem/17070
from collections import deque
def answer(G):
    G[0][0], G[0][1] = 2, 2
    result = 0
    HORIZONTAL = (((0, 1), 0), ((1, 1), 2))
    VERTICAL = (((1, 0), 1), ((1, 1), 2))
    DIAGONAL = (((0, 1), 0), ((1, 0), 1), ((1, 1), 2))
    q = deque()
    q.append(([[0, 0], [0, 1], 0]))     # 가로 : 0 세로 : 1 대각선 : 2

    while q:
        back, front, status = q.popleft()
        if front[0] == len(G) - 1 and front[1] == len(G) - 1:
            result += 1
            continue

        if status == 0:
            for f, s in HORIZONTAL:
                x = front
                y = front[0] + f[0], front[1] + f[1]

                if y[0] >= len(G) or y[1] >= len(G) or G[y[0]][y[1]] == 1:
                    continue
                if s == 2:
                    if G[y[0] - 1][y[1]] == 1 or G[y[0]][y[1] - 1] == 1:
                        continue

                q.append((x, y, s))

        elif status == 1:
            for f, s in VERTICAL:
                x = front
                y = front[0] + f[0], front[1] + f[1]

                if y[0] >= len(G) or y[1] >= len(G) or G[y[0]][y[1]] == 1:
                    continue
                if s == 2:
                    if G[y[0] - 1][y[1]] == 1 or G[y[0]][y[1] - 1] == 1:
                        continue

                q.append((x, y, s))
        else:
            for f, s in DIAGONAL:
                x = front
                y = front[0] + f[0], front[1] + f[1]

                if y[0] >= len(G) or y[1] >= len(G) or G[y[0]][y[1]] == 1:
                    continue
                if s == 2:
                    if G[y[0] - 1][y[1]] == 1 or G[y[0]][y[1] - 1] == 1:
                        continue

                q.append((x, y, s))