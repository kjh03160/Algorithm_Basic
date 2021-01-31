# https://www.acmicpc.net/problem/14502
import copy


def answer(G, virus, zeros):
    max_ = 0
    for L in get_possible_wall(zeros):
        K = copy.deepcopy(G)
        for r, c in L:
            K[r][c] = 1
        all_virus(K, virus)
        # x = cal(K)
        # if max_ < x:
        #     max_ = x
        #     print(*K)
        max_ = max(cal(K), max_)
    return max_


from itertools import combinations


def get_possible_wall(L):
    return list(combinations(L, 3))


def make_virus(G, row, col):
    DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))
    for r, c in DIRECTION:
        drow, dcol = r + row, c + col
        if drow < 0 or dcol < 0 or drow >= len(G) or dcol >= len(G[0]):
            continue
        if G[drow][dcol] == 0:
            G[drow][dcol] = 2
            make_virus(G, drow, dcol)


def all_virus(G, virus):
    for r, c in virus:
        make_virus(G, r, c)


def cal(G):
    s = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == 0:
                s += 1
    return s


import sys

input = sys.stdin.readline
row, col = map(int, input().split())
G = []
virus = []
zeros = []
for _ in range(row):
    x = list(map(int, input().split()))
    virus.extend([(_, i) for i in range(len(x)) if x[i] == 2])
    zeros.extend([(_, i) for i in range(len(x)) if x[i] == 0])
    G.append(x)
print(answer(G, virus, zeros))
