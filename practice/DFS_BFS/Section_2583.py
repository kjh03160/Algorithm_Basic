# https://www.acmicpc.net/problem/2583

def answer(R):
    DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))

    def dfs(row, col, R, DIRECTION, s):
        for r, c in DIRECTION:
            drow = r + row
            dcol = c + col

            if drow < 0 or dcol < 0 or drow >= len(R) - 1 or dcol >= len(R[0]) - 1:
                continue

            if R[drow][dcol] == 0:
                R[drow][dcol] = 1
                s += 1
                s = dfs(drow, dcol, R, DIRECTION, s)
        return s

    count = 0
    result = []
    for row in range(len(R) - 1):
        for col in range(len(R[0]) - 1):
            if R[row][col] == 0:
                R[row][col] = 1
                s = dfs(row, col, R, DIRECTION, 1)
                count += 1
                result.append(s)
    return (count, sorted((result)))
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
m, n, k = map(int, input().split())
R = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
for _ in range(k):
    l_x, l_y, r_x, r_y = map(int, input().split())
    x_length = r_x - l_x
    y_length = r_y - l_y
    for i in range(y_length):
        R[l_y + i][l_x: r_x] = [3 for _ in range(x_length)]

a, b = answer(R)
print(a)
print(*b)