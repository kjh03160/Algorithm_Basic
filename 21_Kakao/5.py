# Success

from collections import defaultdict
import sys, copy
max_sheep = 0
temp = set()
def solution(info, edges):
    answer = 0

    G = defaultdict(set)
    for a, b in edges:
        G[a].add(b)
        G[b].add(a)

    info[0] = -1
    dfs(G, info, 1, 0, 0)
    return max_sheep


import heapq
def bfs(G, info):
    global max_sheep
    q = []

    heapq.heappush(q, [-1, 0, 0, None, info])
    while q:
        sheep, wolf, now, prev, info = heapq.heappop(q)
        max_sheep = max(sheep, max_sheep)
        for next in G[now]:
            if info[next] == 1 and abs(sheep) > wolf + 1:
                info[next] = -1
                heapq.heappush(q, [sheep, wolf + 1, next, now, info[:]])
                pass
            elif info[next] == 0:
                info[next] = -1
                heapq.heappush(q, [sheep - 1, wolf, next, now, info[:]])

    pass

def dfs(G, info, sheep, wolf, now):
    global max_sheep, temp
    max_sheep = max(sheep, max_sheep)
    for next in sorted(list(G[now])):
        if info[next] == 1 and sheep > wolf + 1:
            prev = copy.deepcopy(G[next])
            G[next] = G[next].union(G[now])
            G[next].discard(next)
            G[next].discard(now)
            info[next] = -1
            dfs(G, info, sheep, wolf + 1, next)
            info[next] = 1
            G[next] = prev

        elif info[next] == 0:
            prev = copy.deepcopy(G[next])

            G[next] = G[next].union(G[now])
            G[next].discard(next)
            G[next].discard(now)
            info[next] = -1
            dfs(G, info, sheep + 1, wolf, next)
            info[next] = 0
            G[next] = prev






sys.setrecursionlimit(10 * 9)
print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

