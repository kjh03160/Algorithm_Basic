# https://www.acmicpc.net/problem/1912

def answer(num):
    DP = [-1000]
    for i in range(len(num)):
        DP.append(max(DP[-1] + num[i], num[i]))
    return max(DP)

import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

print(answer(numbers))