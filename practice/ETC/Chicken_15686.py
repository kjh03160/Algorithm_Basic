# boj.kr/15686

def get(num, visited, now):
    global m, index
    now.append(num)
    if len(visited) == m:
        index.append(now[:])
        now.pop()
        return

    for i in range(num + 1, len(chk)):
        if i not in visited:
            visited.add(i)
            get(i, visited, now)
            visited.remove(i)
    now.pop()

def get_index():
    global visited, m, chk
    for i in range(len(chk)):
        if i not in visited:
            visited.add(i)
            get(i, visited, [])
            visited.remove(i)


def answer(G):
    global index, n, house
    get_index()
    ans = float('inf')
    for idx in index:
        K = [[float('inf') for _ in range(n)] for _ in range(n)]

        for k in idx:
            result = 0
            row, col = chk[k]
            for i, j in house:
                K[i][j] = min(abs(i - row) + abs(j - col), K[i][j])
                result += K[i][j]
            ans = min(ans, result)

    return ans


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = []
chk = []
house = []
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(len(x)):
        if x[j] == 2:
            chk.append((i, j))
        elif x[j] == 1:
            house.append((i, j))
    G.append(x)
index = []
visited = set()
print(answer(G))
