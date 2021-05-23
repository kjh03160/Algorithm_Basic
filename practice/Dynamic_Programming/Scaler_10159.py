# boj.kr/10159

def answer(G):
    global n
    DP = [[0 for _ in range(n)] for _ in range(n)]

    for a, b in G:
        DP[a - 1][b - 1] = 1

    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if start == end:
                    continue
                if DP[start][mid] == 1 and DP[mid][end] == 1:
                    DP[start][end] = 1

    for start in range(n):
        count = 0
        for end in range(n):
            if start == end:
                continue

            if (not DP[start][end]) and (not DP[end][start]):
                count += 1
        print(count)



import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
G = [list(map(int, input().split())) for _ in range(m)]
answer(G)