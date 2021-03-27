# https://www.acmicpc.net/problem/3079
def answer(p, T):
    MAX_T = 2 * max(T) * p
    MIN_T = 0
    result = 0
    while MIN_T <= MAX_T:
        MID = (MIN_T + MAX_T) // 2
        temp = 0
        for pod in T:
            temp += MID // pod
        if temp >= p:
            MAX_T = MID - 1
            result = MID
        elif temp < p:
            MIN_T = MID + 1
    return result


import sys
input = sys.stdin.readline
n, p = map(int, input().split())
T = []
for i in range(n):
    T.append(int(input()))
print(answer(p, T))

