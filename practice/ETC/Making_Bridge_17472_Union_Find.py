# https://www.acmicpc.net/problem/17472
def dfs_island(row, col, G, visited, temp):
    global DIRECTION

    if row >= len(G) and col >= len(G[0]):
        return

    for r, c in DIRECTION:
        drow, dcol = r + row, c + col

        if drow < 0 or drow >= len(G) or dcol < 0 or dcol >= len(G[0]) or visited[drow][dcol] or G[drow][dcol] != 1:
            continue
        visited[drow][dcol] = True
        temp.append((drow, dcol))
        dfs_island(drow, dcol, G, visited, temp)


def get_islands(G):
    global islands
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            temp = []
            if G[i][j] == 1 and not visited[i][j]:
                temp.append((i, j))
                visited[i][j] = True
                dfs_island(i, j, G, visited, temp)
                islands[count] = temp
                count += 1
    return count


def test(G, start, dest, row, col, bg, up = False, down = False, right=False, left=False):
    global DIRECTION, dist
    if row >= len(G) or col >= len(G[0]):
        return

    if G[row][col] == 1:
        if (row, col) in islands[dest] and bg != 1:
            dist[dest][start] = min(dist[dest][start], bg)
            dist[start][dest] = dist[dest][start]
        else:
            return

    if up:
        n_r, n_c = row - 1, col
        test(G, start, dest, n_r, n_c, bg + 1, up=True)
    elif down:
        n_r, n_c = row + 1, col
        test(G, start, dest, n_r, n_c, bg + 1, down=True)
    elif right:
        n_r, n_c = row, col + 1
        test(G, start, dest, n_r, n_c, bg + 1, right=True)
    elif left:
        n_r, n_c = row, col - 1
        test(G, start, dest, n_r, n_c, bg + 1, left=True)


def get_dist(islands, DIRECTION):
    for start in islands.keys():
        for dest in islands.keys():
            if start == dest: continue
            for row, col in islands[start]:

                for i, p in enumerate(DIRECTION):
                    r, c = p
                    n_r, n_c = row + r, col + c
                    if i == 0:
                        test(G, start, dest, n_r, n_c, 0, down=True)
                    elif i == 1:
                        test(G, start, dest, n_r, n_c, 0, right=True)
                    elif i == 2:
                        test(G, start, dest, n_r, n_c, 0, up=True)
                    else:
                        test(G, start, dest, n_r, n_c, 0, left=True)


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]
islands = {i: [] for i in range(6)}
num_islands = get_islands(G)
dist = {i: [float('inf') for _ in range(num_islands)] for i in range(num_islands)}
get_dist(islands, DIRECTION)
T = []
for i in range(num_islands):
    for j in range(num_islands):
        if dist[i][j] != float('inf') and (j, i, dist[j][i]) not in T:
            T.append((i, j, dist[i][j]))
T.sort(key=lambda x: x[2])

u = [{i} for i in range(num_islands)]
def answer(T):
    global num_islands
    result = 0
    count = 0
    for edge in T:
        start, end, cost = edge
        if u[start] == u[end]:
            continue
        u[start] = u[start].union(u[end])
        for i in u[start]:
            u[i] = u[start]
        result += cost
        count += 1
        if count == num_islands - 1:
            return result
    return -1
print(answer(T))