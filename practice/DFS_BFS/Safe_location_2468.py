# https://www.acmicpc.net/problem/2468

def answer(row, col, rain, G):
    global DIRECTION, count

    visited[row][col] = True

    for r, c in DIRECTION:
        drow = row + r
        dcol = col + c

        if drow < 0 or dcol < 0 or drow >= len(G) or dcol >= len(G):
            continue

        if not visited[drow][dcol] and G[drow][dcol] > rain:
            visited[drow][dcol] = True
            answer(drow, dcol, rain, G)


import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
G = []
min_ = 101
max_ = 0

DIRECTION = ((0, 1), (1, 0), (-1, 0), (0, -1))
for _ in range(n):
    x = list(map(int, input().split()))
    for i in x:
        if min_ > i:
            min_ = i
        if max_ < i:
            max_ = i
    G.append(x)


result = 1
for i in range(min_, max_):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for row in range(len(G)):
        for col in range(len(G)):
            if not visited[row][col] and G[row][col] > i:
                answer(row, col, i, G)
                count += 1
    if count > result:
        result = count
print(result)
