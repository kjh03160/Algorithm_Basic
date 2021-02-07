# https://www.acmicpc.net/problem/17136

def get_index(G):
    for i in range(10):
        for j in range(10):
            if G[i][j] == 1:
                row, col = i, j
                return row, col

def dfs(G, remain, count):
    global result, P

    if result != -1 and count > result:     # 이미 최소 종이 개수를 넘어 갔으면 종료
        return

    if remain == 0:  # 모든 1을 제거한 경우
        if result == -1:    # 최초 경신 안된 상
            result = count
        else:
            result = min(result, count)
        return

    # 1인 인덱스 찾기
    row, col = get_index(G)

    # row, col 위치에 대입 가능한 색종이 탐색
    for p in range(5, 0, -1):
        if not P[p]:  # 남은 종이 없을 경우
            continue
        if check(G, row, col, p):  # 붙일수 있는지 확인
            update(G, row, col, p, 0)   # 해당 위치 종이 부착
            P[p] -= 1
            dfs(G, remain - p ** 2, count + 1)
            P[p] += 1
            update(G, row, col, p, 1) # 해당 위치 종이 다시 붙이기


def update(G, row, col, p, boolean):
    for r in range(p):
        for c in range(p):
            G[row + r][col + c] = boolean


def check(G, row, col, p):
    flag = True
    if row + p > 10 or col + p > 10:
        return False
    for r in range(p):
        for c in range(p):
            if not G[row + r][col + c]:
                flag = False
                break
    return flag



import sys
input = sys.stdin.readline
G = []
K = 0
for i in range(10):
    x = list(map(int, input().split()))
    for k in range(len(x)):
        if x[k] == 1:
            K += 1
    G.append(x)

result = -1
P = {i: 5 for i in range(1, 6)}

dfs(G, K, 0)
print(result)
