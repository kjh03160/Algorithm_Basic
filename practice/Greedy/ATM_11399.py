# https://www.acmicpc.net/problem/11399

def answer(L):
    L.sort()
    L = [0] + L
    for i in range(1, len(L)):
        L[i] = L[i -1] + L[i]
    return sum(L)

import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
print(answer(time))