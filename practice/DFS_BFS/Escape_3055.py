# https://www.acmicpc.net/problem/3055

from collections import deque


def answer(G, now, dest, waters):
    q = deque()
    visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    count = float('inf')
    q.append(now + (0,))
    water_time = 0
    while q:
        row, col, time = q.popleft()

        if row == dest[0] and col == dest[1]:
            count = min(count, time)
            continue

        if water_time == time:
            water_time += 1
            flood(G, waters)

        for r, c in DIR:
            drow, dcol = r + row, c + col
            if 0 <= drow < len(G) and 0 <= dcol < len(G[0]) and not visited[drow][dcol]:
                visited[drow][dcol] = True
                if G[drow][dcol] != "*" and G[drow][dcol] != "X":
                    q.append((drow, dcol, time + 1))

    return count


def flood(G, waters):
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    new = set()
    for row, col in waters:
        for r, c in DIR:
            drow, dcol = r + row, c + col
            if 0 <= drow < len(G) and 0 <= dcol < len(G[0]) and (drow, dcol) not in waters:
                if G[drow][dcol] != "D" and G[drow][dcol] != "X":
                    G[drow][dcol] = "*"
                    new.add((drow, dcol))
    waters.update(new)


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
G = []
now = None
dest = None
waters = set()
for i in range(n):
    x = input()
    temp = []
    for j in range(m):
        temp.append(x[j])
        if x[j] == "S":
            now = (i, j)
        elif x[j] == "D":
            dest = (i, j)
        elif x[j] == "*":
            waters.add((i, j))
    G.append(temp)

result = answer(G, now, dest, waters)
print(result) if result != float('inf') else print("KAKTUS")


