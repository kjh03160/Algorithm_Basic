# https://www.acmicpc.net/problem/18870
def answer(K):
    T = sorted(K)
    X = {T[0]: 0}
    for i in range(1, len(T)):
        if T[i] in X:
            continue
        X[T[i]] = len(X)

    for k in range(len(K)):
        K[k] = X[K[k]]
    return K

import sys
input = sys.stdin.readline
n = int(input())
K = list(map(int, input().split()))
print(*answer(K))