# boj.kr/17836

from collections import deque
def answer(G, t):
    q = deque()

    row, col = 0, 0
    visited = [[False for _ in range(m)] for _ in range(n)]

    visited[row][col] = True
    have_gram = False if G[row][col] != 2 else True
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    result = float('inf')
    q.append((0, row, col, have_gram))

    while q:
        count, row, col, have_gram = q.popleft()

        if row == n - 1 and col == m - 1:
            result = min(count, result)
            continue

        if count > t:
            continue

        if G[row][col] == 2:
            have_gram = True

        # 그람이 있으면 어디든 갈 수 있으니 바로 계산
        if have_gram:
            result = min(count + abs(row - (n - 1)) + abs(col - (m - 1)), result)
            continue

        for r, c in direction:
            drow, dcol = r + row, c + col
            if 0 <= drow < n and 0 <= dcol < m:
                if not visited[drow][dcol]:
                    # 0, 2 또는 그람을 가지고 있으면
                    if G[drow][dcol] == 0 or G[drow][dcol] == 2 or have_gram:
                        visited[drow][dcol] = True
                        q.append((count + 1, drow, dcol, have_gram))
    return result

import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
r = answer(G, t)
print(r if r != float('inf') and r <= t else "Fail")

