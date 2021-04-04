# https://www.acmicpc.net/problem/9466

def dfs(x):
    global result, L
    visited[x] = True
    cycle.append(x)  # 사이클을 이루는 팀을 확인하기 위함
    number = L[x]

    if visited[number]:  # 방문 했던 곳이다 -> 현재 배열 중에 number가 팀을 이룰 수 있는 사이클이 있다.
        if number in cycle:  # 사이클 가능 여부
            result += cycle[cycle.index(number):]  # 사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    L = [0] + list(map(int, input().split()))

    visited = [False for _ in range(n + 1)]
    result = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(result))
