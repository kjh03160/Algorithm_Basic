# https://www.acmicpc.net/problem/6186

def dfs(row, col):
    for dr, dc in [(0, 1), (1, 0),(0, -1), (-1, 0)]:
        if 0 <= row + dr < r and 0 <= col + dc < c and board[row + dr][col + dc] == '#':
            board[row + dr][col + dc] = '.'
            dfs(row + dr, col + dc)


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
cnt = 0
for row in range(r):
    for col in range(c):
        if board[row][col] == '#':
            cnt += 1
            dfs(row, col)
print(cnt)

from collections import deque
r, c = map(int, input().split())
a = [list(input().strip()) for _ in range(r)]
check = [[False]*c for _ in range(r)]
ans = 0

def bfs(row, col):
    global r, c

    q = deque()
    q.append((row, col))
    check[row][col] = True
    while q:
        now_row, now_col = q.popleft()
        for drow, dcol in (-1, 0), (1, 0), (0, -1), (0, 1):
            nrow, ncol = now_row + drow, now_col + dcol
            if nrow < 0 or ncol < 0 or nrow >= r or ncol >= c:
                continue
            if not check[nrow][ncol] and a[nrow][ncol] == '#':
                q.append((nrow, ncol))
                check[nrow][ncol] = True

for row in range(r):
    for col in range(c):
        if not check[row][col] and a[row][col] == '#':
            bfs(row, col)
            ans += 1
print(ans)

def grass(G):
    result = 0
    for row in range(len(G)):
        for count in range(len(G[row])):
            cur = G[row].pop()
            if cur - 1 in G[row] or (row + 1 < len(G) and cur in G[row + 1]):
                continue
            else:
                result += 1
    return result

n, m = map(int, input().split())
G = []
for i in range(n):
    text = input()
    temp = []
    for j in range(m):
        if text[j] == "#":
            temp.append(j)
    G.append(temp)
print(G)
print(grass(G))