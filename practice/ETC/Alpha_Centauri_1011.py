# https://www.acmicpc.net/problem/1011
import math

def answer(start, end):
    LIMIT = (end - start - 1) * 2

    DP = [int(math.sqrt(2 ** 31))] * LIMIT
    DP[0:2] = [1, 1]
    DP[-1] = 1

    for i in range(0, end - start - 1, 2):
        dist, k = DP[i], DP[i + 1]

        jump = 2 * (k - 1)
        if i + jump >= LIMIT:
            continue
        DP[i + jump], DP[i + jump + 1] = (DP[i] + 1, DP[i + 1]) if DP[i + jump] > DP[i] + 1 else (DP[i + jump], DP[i + jump + 1])

        jump = 2 * k
        if i + jump >= LIMIT:
            continue
        DP[i + jump], DP[i + jump + 1] = (DP[i] + 1, DP[i + 1]) if DP[i + jump] > DP[i] + 1 else (DP[i + jump], DP[i + jump + 1])

        jump = 2 * (k + 1)
        if i + jump >= LIMIT:
            continue
        DP[i + jump], DP[i + jump + 1] = (DP[i] + 1, DP[i + 1]) if DP[i + jump] > DP[i] + 1 else (DP[i + jump], DP[i + jump + 1])

    return DP[-2] + 1

import math
def answer2(start, end):
    n = end - start

    count = 3
    if n <= 3:
        count = n
        return count

    for i in range(2, int(math.sqrt(2 ** 31)) + 1):
        if i * i + 1 <= n < i * (i + 1) + 1:
            count = i + i
            break
        elif i * (i + 1) + 1 <= n < (i + 1) ** 2 + 1:
            count = i + i + 1
            break
    return count


import sys
input = sys.stdin.readline
t = int(input())
T = []
for _ in range(t):
    T.append(list(map(int, input().split())))

for i in T:
    print(answer2(i[0], i[1]))
# print(answer(T[1][0], T[1][1]))

"""
3
0 2147483647
1 2147483647
2 2147483647
"""