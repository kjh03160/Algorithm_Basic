# boj.kr/6416

def answer(G, all):
    # 빈 트리
    if not all:
        return True
    # 나왔던 정점 - v 집합(indegree)
    root = list(all.difference(set(G.keys())))
    # root가 없거나, 2개 이상이면
    if len(root) != 1:
        return False
    for i in G:
        # 들어오는 엣지가 2개 이상이면 -> 2번 조건 위배
        if len(G[i]) >= 2:
            return False
    return True


import sys
input = sys.stdin.readline

i = 1
G = {}
T = {}
all = set()
while True:
    x = input().rstrip()

    if not len(x):
        continue

    if "-" in x:
        break

    for k in x.split("  "):
        a, b = map(int, k.split())
        if a == 0 and b == 0:
            if answer(G, all):
                print("Case %d is a tree." % i)
            else:
                print("Case %d is not a tree." % i)
            i += 1
            G.clear()
            all.clear()
            T.clear()
        else:
            all.add(a)
            all.add(b)
            if G.get(b):
                G[b].append(a)
            else:
                G[b] = [a]

