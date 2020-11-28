# https://www.acmicpc.net/problem/1697


from collections import deque
def answer():
    global n, m

    dist = [0 for _ in range(100001)]
    visited = [False for _ in range(100001)]
    q = deque()
    q.append({0 : [n]})
    count = 0

    while q:
        x = q.popleft()
        for k in list(x.values())[0]:
            if 0 <= k < 100001 and not visited[k]:
                visited[k] = True
                dist[k] = dist[list(x.keys())[0]] + 1
                if k == m:
                    return dist[k] - 1
                q.append({k: [2 * k, k - 1, k + 1]})
        count += 1


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
print(answer())