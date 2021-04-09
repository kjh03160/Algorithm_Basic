# boj.kr/19845


def search(x, left, right):
    global N
    while left < right:
        mid = (left + right) // 2
        if N[mid] >= x:
            left = mid + 1
        else:
            right = mid
    return left


def answer(N, Q):
    global n
    for x, y in Q:
        res = 0
        if N[n] >= x:
            res = 1

        temp = search(x, 1, n)
        if N[y] - x < 0 or temp - y < 0:
            print(0)
        else:
            print(res + N[y] - x + temp - y)


import sys

input = sys.stdin.readline
n, q = map(int, input().split())
N = [0 for _ in range(250001)]
x = list(map(int, input().split()))
for i in range(len(x)):
    N[i + 1] = x[i]
Q = [list(map(int, input().split())) for _ in range(q)]
answer(N, Q)