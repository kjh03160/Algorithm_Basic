# boj.kr/13023

def answer(G):
    global  visited
    visited = [False for _ in range(len(G))]
    for i in range(len(G)):
        if not visited[i]:
            visited[i] = True
            dfs(i, 1)
            visited[i] = False

    print(0)


def dfs(index, count):
    global G, visited

    if count == 5:
        print(1)
        sys.exit()

    for i in G[index]:
        if not visited[i]:
            visited[i] = True
            dfs(i, count + 1)
            visited[i] = False



from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
G = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

answer(G)