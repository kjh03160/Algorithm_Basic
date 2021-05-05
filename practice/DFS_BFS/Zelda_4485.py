# boj.kr/4485

import heapq
def answer(G):
    q = []
    q.append((G[0][0], 0, 0))
    result = float('inf')
    visited = [[False for _ in range(len(G))] for _ in range(len(G))]
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited[0][0] = True
    while q:
        v, r, c = heapq.heappop(q)

        if r == len(G) - 1 and c == len(G) - 1:
            return v

        if v >= result:
            continue

        for row, col in direction:
            drow, dcol = r + row, c + col
            if 0 <= drow < len(G) and 0 <= dcol < len(G) and not visited[drow][dcol]:
                visited[drow][dcol] = True
                heapq.heappush(q, (v + G[drow][dcol], drow, dcol))


import sys
input = sys.stdin.readline
k = 0
while True:
    n = int(input())
    if n == 0:
        break
    G = [list(map(int, input().split())) for _ in range(n)]
    k += 1
    print("Problem %d: %d" % (k, answer(G)))
