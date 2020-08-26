# 13301
n = int(input())

DP = [1, 1]
for i in range(2, n + 1):
    DP.append(DP[i - 1] + DP[i - 2])

print((DP[n - 1] + DP[n]) * 2)
