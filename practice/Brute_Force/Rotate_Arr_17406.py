# https://www.acmicpc.net/problem/17406
import copy
def answer(G, X, cands):
    result = 100 * 51
    for i in cands:
        G1 = copy.deepcopy(G)
        for j in i:
            r, c, s = X[j]
            G2 = copy.deepcopy(G1)
            m_row, m_col = r + s - 1, c + s - 1
            m__row, m__col = r - s - 1, c - s - 1

            for k in range(s):
                max_row, max_col = m_row - k, m_col - k
                min_row, min_col = m__row + k, m__col + k

                a, b, c, d = G1[min_row][min_col], G1[min_row][max_col], G1[max_row][max_col], G1[max_row][min_col]
                for col in range(min_col, max_col + 1): # 위 오른
                    G1[min_row][col] = G2[min_row][col - 1]

                for row in range(min_row + 1, max_row + 1): # 아래
                    if row == min_row + 1:
                        G1[row][max_col] = b
                    else:
                        G1[row][max_col] = G2[row - 1][max_col]

                for col in range(max_col - 1, min_col - 1, -1):
                    if col == max_col - 1:
                        G1[max_row][col] = c
                    else:
                        G1[max_row][col] = G2[max_row][col + 1]

                for row in range(max_row - 1, min_row - 1, -1):
                    if row == max_row - 1:
                        G1[row][min_col] = d
                    else:
                        G1[row][min_col] = G2[row + 1][min_col]

        temp = 100 * 51
        for r in G1:
            temp = min(temp, sum(r))
        result = min(temp, result)
    return result

import sys
from itertools import permutations

input = sys.stdin.readline
n, m, k = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
X = [tuple(map(int, input().split())) for _ in range(k)]
cands = list(permutations([i for i in range(k)], k))
print(answer(G, X, cands))