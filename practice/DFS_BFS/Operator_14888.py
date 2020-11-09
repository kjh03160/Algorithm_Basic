# https://www.acmicpc.net/problem/14888

def answer(index, val, plus, minus, multi, div):
    global n, numbers, max_, min_, ops
    if index == n:
        max_ = max(val, max_)
        min_ = min(val, min_)
        return
    else:   # 만약 op로 직접 접근하면 값이 바뀌기에 값이 제대로 안나옴
        if plus:
            answer(index + 1, val + numbers[index], plus - 1, minus, multi, div)
        if minus:
            ops[1] -= 1
            answer(index + 1, val - numbers[index], plus, minus - 1, multi, div)
        if multi:
            ops[2] -= 1
            answer(index + 1, val * numbers[index], plus, minus, multi - 1, div)
        if div:
            ops[3] -= 1
            answer(index + 1, int(val / numbers[index]), plus, minus, multi, div - 1)


import sys
input = sys.stdin.readline
max_, min_ = -1000000001, 1000000001
result = []
n = int(input())
numbers = list(map(int, input().split()))
ops = list(map(int, input().split()))
answer(1, numbers[0], ops[0], ops[1], ops[2], ops[3])
print(max_, min_)