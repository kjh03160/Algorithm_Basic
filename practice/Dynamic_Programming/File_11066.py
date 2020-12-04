# https://www.acmicpc.net/problem/11066

def answer(F):
    DP = [[0 for _ in range(len(F))] for _ in range(len(F))]    # i번째 장부터 j번째 장까지 채우는데 드는 비용
    sum_v = [0] # i번째까지 합치는데 드는 비용
    temp = 0
    for i in range(len(F)):
        temp += F[i]
        sum_v.append(temp)

    for x in range(1, len(F)):
        for start in range(len(F) - x):
            end = start + x
            DP[start][end] = 9999999999

            for k in range(start, end):
                DP[start][end] = min(DP[start][k] + DP[k + 1][end] + sum_v[end + 1] - sum_v[start], DP[start][end])

    return DP[0][-1]


import sys
input = sys.stdin.readline
t = int(input())
test = []
for i in range(t):
    k = int(input())
    F = list(map(int, input().strip().split()))
    test.append((k, F))
for k, F in test:
    print(answer(F))


import sys
input = sys.stdin.readline
t = int(input())
for __ in range(t):
    k = int(input())
    page = list(map(int, input().split()))
    table = [[0]*k for _ in range(k) ]
    for i in range(k-1):
        table[i][i+1] = page[i] + page[i+1]
        for j in range(i+2, k):
            table[i][j] = table[i][j-1] + page[j]
    for d in range(2, k): # diagonal
        for i in range(k-d):
            j = i+d
            minimum = [table[i][k] + table[k+1][j] for k in range(i, j)]
            table[i][j] += min(minimum)
    print(table[0][k-1])