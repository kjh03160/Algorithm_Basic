# https://www.acmicpc.net/problem/16637
# https://jow1025.tistory.com/132
def dfs(sum, cur, op, nums):
    global ans
    if cur == len(op):
        ans = max(ans, sum)
        return

    # 1 + 2 * 8

    # 이전 값과 현재 숫자를 현재 연산을 계산
    # 1 + 2
    res = cal(sum, nums[cur + 1], op[cur])
    # 앞에 괄호를 친 것은 안친거나 다름 없다?
    # 괄호를 치지 않았을 때
    dfs(res, cur + 1, op, nums)

    # 뒤에 남은 것들이 있다면
    if cur + 1 < len(op):
        # 뒤에 연산을 먼저 계산 -> 뒤에 괄호 친 것
        # 2 * 8
        a = cal(nums[cur + 1], nums[cur + 2], op[cur + 1])
        # 현재 숫자와 연산
        # 1 + (2 * 8)
        b = cal(sum, a, op[cur])
        # 뒤에 괄호 쳤을 떄
        dfs(b, cur + 2, op, nums)


def cal(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b


import sys

input = sys.stdin.readline
n = int(input())
s = input()
op = []
nums = []
for i in range(n):
    if i % 2 == 0:
        nums.append(int(s[i]))
    else:
        op.append(s[i])
ans = -(2 ** 31)
dfs(nums[0], 0, op, nums)
print(ans)
