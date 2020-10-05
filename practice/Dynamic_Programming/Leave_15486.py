# https://www.acmicpc.net/problem/15486

def max_profit(N, works):
    dp = [0] * (N + 2)
    for i in range(1, N + 1):
        cost_Time, profit_value = works[i][0], works[i][1]
        if cost_Time + i <= N + 1:
            dp[i + cost_Time] = max(dp[i] + profit_value, dp[i + cost_Time])
        dp[i + 1] = max(dp[i + 1], dp[i])
    return max(dp)

n = int(input())
works = [(0, 0)]
for i in range(n):
    works.append(tuple(map(int, input().split())))

print(max_profit(n, works))
