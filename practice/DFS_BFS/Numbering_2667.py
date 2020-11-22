# https://www.acmicpc.net/problem/2667

def answer(row, col):
    global ans, count, number, direction, K
    if not visited[row][col] and K[row][col] == '1':
        count += 1
        visited[row][col] = True
        for i in direction:
            drow = row + i[0]
            dcol = col + i[1]
            if (drow < n and dcol < n) and (drow >= 0 and dcol >= 0):
                answer(row + i[0], col + i[1])
    ans[number] = count



import sys
input = sys.stdin.readline
n = int(input())
K = []
ans = {}
count = 0
number = 1
direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

visited = [[False for _ in range(n)] for __ in range(n)]
for _ in range(n):
    K.append(input().strip())
for i in range(n):
    for j in range(n):
        if K[i][j] == '1' and not visited[i][j]:
            answer(i, j)
            number += 1
            count = 0

print(len(ans))
print(*sorted(ans.values()), sep='\n')