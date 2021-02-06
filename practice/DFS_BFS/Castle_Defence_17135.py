# https://www.acmicpc.net/problem/17135

from collections import deque
import copy
def answer(G, arrows, n, m, d):
    max_ = 0
    for arr in arrows:
        C = copy.deepcopy(G)
        result = 0

        q = deque()
        start = 1
        while start != n + 1:
            append_enemy(C, q, arr, start, n, m, d)
            while q:
                e_row, e_col = q.popleft()
                if C[e_row][e_col] == 1:
                    result += 1
                C[e_row][e_col] = -1

            start += 1
        max_ = max(max_, result)
    return max_


def append_enemy(G, q, arr, start,  n, m, d):
    for k in arr:
        ps_enem = None
        min_dist = 11
        for row in range(start, n + 1):
            if row > d + start:
                break
            for col in range(m):
                dist = cal_dist(start - 1, k, row, col)

                if dist <= d and G[row][col] >= 1:
                    if min_dist > dist:
                        ps_enem = (row, col)
                        min_dist = dist
                    if min_dist == dist and ps_enem and ps_enem[1] > col:
                        ps_enem = (row, col)

        if ps_enem:
            q.append(ps_enem)
    return q


def cal_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


import sys
from itertools import combinations
input = sys.stdin.readline
n, m, d = map(int, input().split())
G = [[0 for _ in range(m)] for _ in range(n + 1)]
for i in range(n, 0, -1):
    G[i] = list(map(int, input().split()))

arrows = list(combinations([i for i in range(m)], 3))
print(answer(G, arrows, n, m, d))