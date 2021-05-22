
from collections import deque
def answer(G, units):
    chk = False

    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] == "D":
                for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    drow, dcol = i + r, j + c
                    if 0 <= drow < len(G) and 0 <= dcol < len(G):
                        if G[drow][dcol] != "X":
                            chk = True
                            break
    if not chk:
        return -1

    for i, j in units:
        chk = False
        for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            drow, dcol = i + r, j + c
            if 0 <= drow < len(G) and 0 <= dcol < len(G):
                if G[drow][dcol] != "X":
                    chk = True
                    break
    if not chk:
        return -1

    q = deque()
    q.append((0, *units))
    finish = 0
    min_time = 50 ** 3
    out = [False for _ in range(len(units))]
    while q:
        time, *units = q.popleft()
        row1, col1 = units[0]
        row2, col2 = units[1]

        if time > min_time:
            continue

        if G[row1][col1] == "D":
            if not out[0]:
                finish += 1
                out[0] = True

        if G[row2][col2] == "D":
            if not out[1]:
                finish += 1
                out[1] = True

        if finish >= len(units):
            min_time = min(min_time, time)
            break

        for r, c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            drow1, dcol1 = r + row1, c + col1
            drow2, dcol2 = r + row2, c + col2
            tmp = []
            if 0 <= drow1 < len(G) and 0 <= dcol1 < len(G) and G[drow1][dcol1] != "X":
                tmp.append((drow1, dcol1))
            else:
                tmp.append((row1, col1))
            if 0 <= drow2 < len(G) and 0 <= dcol2 < len(G) and G[drow2][dcol2] != "X":
                tmp.append((drow2, dcol2))
            else:
                tmp.append((row2, col2))
            if tmp:
                q.append((time + 1, *tmp))

    return min_time if min_time != float('inf') else -1


import sys
input = sys.stdin.readline
n = int(input())
G = [input().rstrip() for _ in range(n)]
units = []
tmp = list(map(int, input().split()))
for i in range(0, len(tmp), 2):
    units.append((tmp[i], tmp[i + 1]))
print(answer(G, units))

"""
5
...DD
.....
XXXXX
X....
.....
4 2 2 4 
"""