# https://www.acmicpc.net/problem/10819

def start(L):
    result_val = []
    for i in range(len(L)):
        visited = [False] * len(L)
        visited[i] = True
        temp = [L[i]]
        backtrack(L, temp, visited, result_val)
        temp.clear()
    return max(result_val)


def backtrack(L, temp, visited, result_val):
    if len(L) == len(temp):
        x = cal(temp)
        result_val.append(x)
        return

    for j in range(len(L)):
        if not visited[j]:
            temp.append(L[j])
            visited[j] = True
            # print(temp, j, visited)
            backtrack(L, temp, visited, result_val)
            visited[j] = False
            temp.pop()


def cal(temp):
    a = 0
    for i in range(len(temp) - 1):
        a += abs(temp[i] - temp[i - 1])
    return a


import sys

# sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))

print(start(L))
