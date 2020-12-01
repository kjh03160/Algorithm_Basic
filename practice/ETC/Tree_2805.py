# acmicpc.net/problem/2805

def answer(t):
    global m
    lowest, highest = 0, max(t)

    while lowest != highest:
        middle = (lowest + highest + 1) // 2
        bring = sum([(h - middle if h > middle else 0) for h in t])

        if bring >= m:
            lowest = middle
        else:
            highest = middle - 1
    return highest

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
t = list(map(int, input().split()))
print(answer(t))