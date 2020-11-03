# https://www.acmicpc.net/problem/11053

def answer(A):
    DP = [1] * len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if A[i] > A[j]:
                DP[i] = (max(DP[i], DP[j] + 1))
    return max(DP)


import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
print(answer(A))