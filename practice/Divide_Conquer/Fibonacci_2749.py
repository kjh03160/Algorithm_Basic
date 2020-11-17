# https://www.acmicpc.net/problem/2749

def answer(n):
    base = [[1, 1], [1, 0]]
    if n <= 1:
        return base

    def mul(a, b):
        result = [[0 for _ in range(2)] for k in range(2)]

        for i in range(2):
            for j in range(2):
                for x in range(2):
                    result[i][j] += (a[i][x] * b[x][j]) % 1000000
        return result

    if n % 2:
        x = answer(n - 1)
        return mul(base, x)
    x = answer(n // 2)
    return mul(x, x)


    pass

import sys
input = sys.stdin.readline
n = int(input())
print(answer(n)[1][0] % 1000000)
