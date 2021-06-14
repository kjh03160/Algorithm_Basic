# boj.kr/14400

def answer(X, Y, P):
    X.sort()
    Y.sort()

    mid_x = X[len(X) // 2]
    mid_y = Y[len(Y) // 2]

    dist = 0

    for x, y in P:
        dist += abs(x - mid_x) + abs(y - mid_y)
    return dist


import sys
input = sys.stdin.readline
n = int(input())
X = []
Y = []
P = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    P.append((x, y))
print(answer(X, Y, P))