# boj.kr/2458

def ansewr(dist):
    global n

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][mid] and dist[mid][end]:
                    print(start, mid, end)
                    dist[start][end] = 1
    print(*dist, sep='\n')
    result = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if dist[i][j] or dist[j][i]:
                count += 1
        if count == n - 1:
            result += 1
    return result

# 자신에서 학생으로 갈 수 있거나, 학생에서 자신으로 올 수 있으면 자신이 몇번째인지 알 수 있다
# 플로이드 와샬을 통해 각 학생들간의 거리를 구하고, 자신을 제외한 모든 학생에 대한 거리가 있는 경우를 찾으면 된다.
# 그냥 dfs로도 됨
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dist = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    dist[a - 1][b - 1] = 1
print(ansewr(dist))