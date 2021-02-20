#https://www.acmicpc.net/problem/11657
def answer(G, dist, n):

    for i in range(n):
        for node in range(len(G)):
            start, end, cost = G[node][0], G[node][1], G[node][2]
            if dist[start] != float('inf') and dist[end] > dist[start] + cost:
                dist[end] = dist[start] + cost

                if i == n - 1:  # 마지막 라운드에서도 갱신이 된다면 음수 순환이 존재
                    return True

    return False


import sys
input = sys.stdin.readline
n, e = map(int, input().split())
G = []
for _ in range(e):
    a, b, c = map(int, input().split())
    G.append((a, b, c))

dist = [float('inf') for _ in range(n + 1)]
dist[1] = 0
x = answer(G, dist, n)

if not x:
    for i in range(2, n + 1):
        print(-1 if dist[i] == float('inf') else dist[i])
else:
    print(-1)