# boj.kr/7453

def answer(A, B, C, D):
    X = {}
    for i in range(len(C)):
        for j in range(len(D)):
            v = C[i] + D[j]
            if v in X:
                X[v] += 1
            else:
                X[v] = 1

    result = 0

    for i in range(len(A)):
        for j in range(len(B)):
            v = A[i] + B[j]
            if -v in X:
                result += X[-v]
    return result


import sys
input = sys.stdin.readline

n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
print(answer(A, B, C, D))