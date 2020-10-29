# https://www.acmicpc.net/problem/10989
import sys
input = sys.stdin.readline

N = int(input())

count = [0] * (10000 + 1)

for i in range(N):
    num = int(input())
    count[num] += 1

for j in range(len(count)):
    if count[j] != 0:
        a = count[j]
        for x in range(a):
            print(j)