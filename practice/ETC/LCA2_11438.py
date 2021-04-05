# boj.kr/11438

def dfs(index, visited, parent, depth):
    global G, D

    visited[index] = True
    D[index] = depth

    for i in G[index]:
        if not visited[i]:
            # 첫번째 자리에 바로 위의 부모 기록
            parent[i][0] = index
            dfs(i, visited, parent, depth + 1)


def set_parent():
    global parent, n, LOG

    visited = [False for _ in range(n + 1)]
    dfs(1, visited, parent, 1)
    # [가장 인접 부모, 그다음 부모, 그다음 부모, ...]
    for i in range(1, LOG):     # 2 제곱 인덱스
        # 모든 노드에 관해서 상위 부모 하나씩 기록
        for j in range(1, n + 1):   # 노드
            # j번 노드로부터 2 ** i단계 위에 있는 부모 = j의 2 ** (i - 1)단계 위 부모의 2 ** (i - 1)단계 위 부모
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(a, b, depth, parent):
    global LOG
    # 항상 b가 더 깊도록 만들고
    if depth[a] > depth[b]:
        a, b = b, a

    # 깊이가 동일하도록 설정
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= 2 ** i:  # 8 -> 4 -> 2 -> 1
            b = parent[b][i]

    # 같다면 바로 리턴
    if a == b:
        return a

    # 같은 조상 찾아 올라가기
    for i in range(LOG - 1, -1, -1):
        # 만약 13번째에 있다면 8 -> 4 -> 1
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]



import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 5)
n = int(input())
G = {i: set() for i in range(1, n + 1)}
D = [0 for _ in range(n + 1)]
LOG = 21  # 2 ** 20 -> 1,000,000

for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)
parent = [[0 for _ in range(LOG)] for _ in range(n + 1)]

set_parent()
print(*parent, sep='\n')
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b, D, parent))