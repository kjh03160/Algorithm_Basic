# https://www.acmicpc.net/problem/14503

from collections import deque
def answer(row, col, d,  G):
    DIRECTION = ((-1, 0), (0, 1), (1, 0), (0, -1))
    stack = [(row, col, d)]
    count = 1
    while stack:
        nrow, ncol, nd = stack.pop()
        # 1
        G[nrow][ncol] = 2
        dd = nd
        # 2
        while True:
            dd = dd - 1 if dd else 3    # 왼쪽 방향 회전
            drow, dcol = nrow + DIRECTION[dd][0], ncol + DIRECTION[dd][1]
            if drow < 0 or dcol < 0 or drow > len(G) or dcol > len(G[0]):
                continue
            # 2.1
            if G[drow][dcol] == 0:
                count += 1
                stack.append((drow, dcol, dd))
                break

            # 2.3
            if dd == nd and G[drow][dcol] != 0:
                dd = nd + 2 if nd < 2 else nd - 2   # 후진
                drow, dcol = nrow + DIRECTION[dd][0], ncol + DIRECTION[dd][1]
                # 2.4
                if G[drow][dcol] == 1 or drow < 0 or dcol < 0 or drow > len(G) or dcol > len(G[0]):
                    return count
                stack.append((drow, dcol, nd))
                break


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = []
r, c, d = map(int, input().split())
for _ in range(n):
    G.append(list(map(int, input().split())))

print(answer(r, c, d, G))