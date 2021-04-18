# boj.kr/15787

def answer(M):
    global n
    N = [[0 for _ in range(21)] for _ in range(n + 1)]
    for cmd in M:
        i = cmd[1]
        if cmd[0] == 1:
            x = cmd[2]
            N[i][x] = 1

        elif cmd[0] == 2:
            x = cmd[2]
            N[i][x] = 0

        elif cmd[0] == 3:
            for k in range(20, 1, -1):
                N[i][k] = N[i][k - 1]
            N[i][1] = 0

        else:
            for k in range(1, 20):
                N[i][k] = N[i][k + 1]
            N[i][20] = 0

    check = set()
    for i in range(1, n + 1):
        now = ""
        for k in N[i]:
            if k:
                now += '1'
            else:
                now += '0'
        check.add(now)
    return len(check)



import sys
input = sys.stdin.readline
n, m = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(m)]
print(answer(M))