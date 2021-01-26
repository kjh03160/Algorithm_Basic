# https://www.acmicpc.net/problem/2447

import math


def answer(s, n):
    for row in range(n):
        for col in range(n):
            for i in range(round(math.log(n, 3))):
                if (row // (3 ** i)) % 3 == 1 and (col // (3 ** i)) % 3 == 1:
                    s[row][col] = " "
        print(*s[row], sep='')

import sys
input = sys.stdin.readline
n = int(input())
s = [["*" for _ in range(n)] for _ in range(n)]

answer(s, n)