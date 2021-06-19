# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
answer = []
import copy
def backtrack(G, col, sum_u, sum_l, C, U, L):
    if col == len(C):
        if sum_u == U and sum_l == L:
            answer.append(copy.deepcopy(G))
        return
    if C[col] == 2:
        G[0][col], G[1][col] = 1, 1
        backtrack(G, col + 1, sum_u + 1, sum_l + 1, C, U, L)
        G[0][col], G[1][col] = 0, 0
    elif C[col] == 1:
        if sum_u + 1 <= U:
            G[0][col] = 1
            backtrack(G, col + 1, sum_u + 1, sum_l, C, U, L)
            G[0][col] = 0
        if sum_l + 1 <= L:
            G[1][col] = 1
            backtrack(G, col + 1, sum_u, sum_l + 1, C, U, L)
            G[1][col] = 0
    else:
        backtrack(G, col + 1, sum_u, sum_l, C, U, L)


def solution(U, L, C):
    G = [[0 for _ in range(len(C))] for _ in range(2)]

    backtrack(G, 0, 0, 0, C, U, L)
    if answer:
        return "%s,%s" % ("".join(map(str, answer[0][0])), "".join(map(str, answer[0][1])))
    else:
        return "IMPOSSIBLE"