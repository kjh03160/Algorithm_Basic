# https://www.acmicpc.net/problem/13460

def move(G, x, y, r, c):
    cnt = 0
    while True:
        nx, ny = x + r, y + c
        cnt += 1
        if G[nx][ny] == 'O':  # 구멍에 빠지면 그 칸
            return (nx, ny, cnt)
        elif G[nx][ny] == '#':  # 벽에 닿으면 그 전칸
            return (x, y, cnt - 1)
        x, y = nx, ny


from collections import deque
def answer(G, red, blue):
    global n, m
    q = deque()
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q.append((1, *red, *blue))
    visited = [[[[False for _ in range(len(G[0]))] for _ in range(len(G))] for _ in range(len(G[0]))] for _ in range(len(G))]
    visited[red[0]][red[1]][blue[0]][blue[1]] = True

    while q:
        time, red_r, red_c, blue_r, blue_c = q.popleft()

        if time > 10:
            continue

        for r, c in direction:
            red_dr, red_dc, r_count = move(G, red_r, red_c, r, c)
            blue_dr, blue_dc, b_count = move(G, blue_r, blue_c, r, c)

            if G[blue_dr][blue_dc] != "O":
                if G[red_dr][red_dc] == "O":
                    return time

                if red_dr == blue_dr and red_dc == blue_dc:
                    if r_count > b_count:
                        red_dr -= r
                        red_dc -= c
                    else:
                        blue_dr -= r
                        blue_dc -= c

                if not visited[red_dr][red_dc][blue_dr][blue_dc]:
                    q.append((time + 1, red_dr, red_dc, blue_dr, blue_dc))
                    visited[red_dr][red_dc][blue_dr][blue_dc] = True
    return -1


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = []
red = None
blue = None
for i in range(n):
    x = input().rstrip()
    for j in range(m):
        if x[j] == "R":
            red = i, j
        elif x[j] == "B":
            blue = i, j
    G.append(x)

print(answer(G, red, blue))
