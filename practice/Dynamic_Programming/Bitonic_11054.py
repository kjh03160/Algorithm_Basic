# https://www.acmicpc.net/problem/11054

def answer(A):
    start = [0] * len(A)
    end = [0] * len(A)
    count = 0
    for i in range(len(A)):
        start[i] = 1
        for j in range(i):
            if A[j] < A[i]:
                start[i] = max(start[i], start[j] + 1)

    for i in range(len(A) - 1, -1, -1):
        end[i] = 1
        for j in range(len(A) - 1, i - 1, -1):
            if A[j] < A[i]:
                end[i] = max(end[i], end[j] + 1)

    for i in range(len(A)):
        if count < start[i] + end[i] - 1:
            count = start[i] + end[i] - 1
    return count

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
print(answer(A))