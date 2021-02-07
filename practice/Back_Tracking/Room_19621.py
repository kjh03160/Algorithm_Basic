# https://www.acmicpc.net/problem/19621

def answer(L):
    backtrack(L, 0, 0)


def backtrack(L, index, people):
    global result

    if index > len(L) - 1:
        result = max(people, result)
        return
    # 회의 시간이 앞뒤로 겹치기에 바로 다음 회의는 건너뜀
    backtrack(L, index + 1, people)
    # 다다음 회의를 넣었을 때
    backtrack(L, index + 2, people + L[index][2])


import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))

result = 0
answer(L)
print(result)
