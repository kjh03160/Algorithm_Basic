# https://www.acmicpc.net/problem/2606

def answer(K):
    global v, count
    for edge in K:
        if not v[edge]:
            count += 1
            v[edge] = True
            answer(L[edge])


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
L = [[] for _ in range(n + 1)]
count = 0
for _ in range(m):
    index, to = map(int, input().split())
    L[index].append(to)
    L[to].append(index)
v = [False] * (len(L) + 1)
v[1] = True
answer(L[1])
print(count)