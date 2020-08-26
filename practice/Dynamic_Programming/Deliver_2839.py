n = int(input())

DP = [99999, 99999, 99999, 1, 99999, 1]
for i in range(6, n + 1):
    if DP[i - 3] or DP[i - 5]:
        DP.append(min(DP[i - 3], DP[i - 5]) + 1)
print(DP[n] if DP[n] < 99999 else -1)