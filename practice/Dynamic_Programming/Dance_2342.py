# boj.kr/2342
def move(fr, to):
    if fr == to:
        return 1
    if fr == 0:
        return 2
    return 4 if abs(fr - to) == 2 else 3

def dfs(left, right, index):
    if index == len(nums) - 1:
        return 0
    if dp[left][right][index] != -1:
        return dp[left][right][index]

    left_move = move(left, nums[index])
    right_move = move(right, nums[index])

    result = min(left_move + dfs(nums[index], right, index + 1), right_move + dfs(left, nums[index], index + 1))
    dp[left][right][index] = result
    return dp[left][right][index]

import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
nums = list(map(int, input().split()))
dp = [[[-1 for _ in range(len(nums))] for _ in range(5)] for _ in range(5)]

print(dfs(0, 0, 0))
