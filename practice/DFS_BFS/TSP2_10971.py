# https://www.acmicpc.net/problem/2098

def dfs(index, finish, value):
    global G, result, visited

    if finish == len(G) and index == 0:
        result = min(result, value)
    else:
        for i in range(len(G[index])):
            if G[index][i] == 0 or visited[i]:
                continue
            visited[i] = True
            if value + G[index][i] < result:
                dfs(i, finish + 1, value + G[index][i])
            visited[i] = False

import sys
input = sys.stdin.readline
n = int(input())
G = {i : [] for i in range(n)}
visited = [False] * n
for _ in range(n):
    x = list(map(int, input().split()))
    G[_].extend(x)

result = 1000000 * 17
dfs(0, 0, 0)
print(result)


"""
16
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
"""