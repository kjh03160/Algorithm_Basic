# https://www.acmicpc.net/problem/20165
import copy
def answer(G, r, attack, defense):
    D = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    R = copy.deepcopy(G)
    score = 0
    for i in range(r):
        row, col, direction = attack[i]
        row, col = map(int, [row, col])
        direction = D[direction]

        dr, dc = defense[i]

        if G[row - 1][col - 1] > 0:
            score += process(G, row - 1, col - 1, direction, R)

        G[dr - 1][dc - 1] = R[dr - 1][dc - 1]
    return score

def process(G, row, col, direction, R):
    count = 1
    k = R[row][col] - 1
    G[row][col] = 0
    while k:
        k -= 1
        row, col = row + direction[0], col + direction[1]

        if row < 0 or row >= len(G) or col < 0 or col >= len(G[0]):
            break

        if G[row][col]:
            count += 1
            if k < R[row][col]:
                k = R[row][col] - 1

        G[row][col] = 0
    return count


import sys
input = sys.stdin.readline
n, m, r = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]

attack = []
defense = []
for _ in range(r):
    attack.append(input().split())
    defense.append(tuple(map(int, input().split())))

print(answer(G, r, attack, defense))

for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] == 0:
            print("F", end=" ")
        else:
            print("S", end=" ")
    print()

