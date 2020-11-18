# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    DP = [[1] * m for __ in range(n)]

    for p in puddles:
        DP[p[1] - 1][p[0] - 1] = 0

    DP[0][0] = 0
    for row in range(n):
        for col in range(m):
            if DP[row][col] == 0:
                continue

            if row == 0:
                if col - 1 == 0:
                    DP[row][col] = 1
                else:
                    DP[row][col] = DP[row][col - 1]
            elif col == 0:
                if row - 1 == 0:
                    DP[row][col] = 1
                else:
                    DP[row][col] = DP[row - 1][col]
            else:
                DP[row][col] = (DP[row - 1][col] + DP[row][col - 1]) % 1000000007

    for i in DP:
        print(i)
    return DP[n - 1][m - 1]


print(solution(1, 4, [[1, 3]]))
print()
print(solution(4, 3, [[2, 2]]))