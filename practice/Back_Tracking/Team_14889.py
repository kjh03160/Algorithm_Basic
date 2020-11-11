# https://www.acmicpc.net/problem/14889

def answer(index, other):
    global n, min_val
    if index == n // 2:
        team1 = 0
        team2 = 0
        for i in range(n):
            for j in range(n):
                if team[i] ==0 and team[j] == 0:
                    team1 += s[i][j]
                elif team[i] == 1 and team[j] == 1:
                    team2 += s[i][j]
        val = abs(team1 - team2)
        if val < min_val:
            min_val = val
        return
    else:
        for i in range(other + 1, n):
            team[i] = 1
            answer(index + 1, i)
            team[i] = 0


import sys
input = sys.stdin.readline
min_val = 9999999
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
team = [0 for _ in range(n)]
answer(0, 0)
print(min_val)