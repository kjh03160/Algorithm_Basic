# boj.kr/2493

def answer(L):
    stack = []
    ans = [0 for _ in range(len(L))]
    for i in range(len(L) - 1, -1, -1):
        while stack and L[stack[-1]] < L[i]:
            ans[stack.pop()] = i + 1
        stack.append(i)

    return ans

import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
print(*answer(L))
