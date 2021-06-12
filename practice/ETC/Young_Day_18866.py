# boj.kr/18866

def answer(Y, O):
    global D
    max_g, min_g = -1, float('inf')
    max_t, min_t = -1, float('inf')

    for i in range(1, n + 1):
        if D[i][0] != 0:
            min_g = min(min_g, D[i][0])
        if D[i][1] != 0:
            max_t = max(max_t, D[i][1])
        Y[i] = [min_g, max_t]

    for i in range(n, -1, -1):
        if D[i][0] != 0:
            max_g = max(max_g, D[i][0])
        if D[i][1] != 0:
            min_t = min(min_t, D[i][1])
        O[i] = [max_g, min_t]

    result = -1
    for i in range(n - 1, -1, -1):
        young_g, young_t = Y[i]
        old_g, old_t = O[i + 1]
        if young_g > old_g and young_t < old_t:
            result = max(result, i)

    return result


import sys
input = sys.stdin.readline
n = int(input())
D = [(0, 0)]

for _ in range(n):
    a, b = map(int, input().split())
    D.append((a, b))
Y = [[0, 0] for _ in range(n + 1)]
O = [[0, 0] for _ in range(n + 1)]
print(answer(Y, O))
