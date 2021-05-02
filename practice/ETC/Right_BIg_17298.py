# boj.kr/17298

def answer(N):
    stack = []
    ans = [-1 for _ in range(len(N))]
    for i in range(len(N)):
        now = N[i]
        while stack and N[stack[-1]] < now:
            index = stack.pop()
            ans[index] = i
        stack.append(i)
    return ans

import sys

input = sys.stdin.readline
n = int(input())
N = list(map(int, input().split()))
print(*answer(N))