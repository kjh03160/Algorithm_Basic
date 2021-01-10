# https://www.acmicpc.net/problem/6603

def backtrack(num_list, index, visited, result_num):
    result_num.append(num_list[index])
    if len(result_num) == 6:
        print(*result_num, sep=" ")
        result_num.pop()
        return

    for j in range(index + 1, len(num_list)):
        if not visited[j]:
            visited[j] = True
            backtrack(num_list, j, visited, result_num)
            visited[j] = False
    result_num.pop()


def start(num_list, visited):
    for i in range(len(num_list) - 5):
        result_num = []
        backtrack(num_list, i, visited, result_num)
        result_num.clear()

import sys
input = sys.stdin.readline
L = []
V = []
while True:
    x = list(map(int, input().split()))
    if x[0] == 0:
        break
    L.append(x[1:])
    V.append([False for _ in range(x[0])])

for i in range(len(L)):
    start(L[i], V[i])
    print()