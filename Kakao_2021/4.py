# https://programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):
    answer = 0
    G = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        G[i][i] = 0
    for x, y, c in fares:
        G[x - 1][y - 1] = c
        G[y - 1][x - 1] = c

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if G[start][end] > G[start][mid] + G[mid][end]:
                    G[start][end] = G[start][mid] + G[mid][end]

    answer = G[s - 1][a - 1] + G[s - 1][b - 1]

    for i in range(n):
        answer = min(answer, G[i][a - 1] + G[i][b - 1] + G[s - 1][i])
    return answer