# https://www.acmicpc.net/problem/2293
def coin(k):
    DP = [0] * (k + 1)
    DP[0] = 1
    for value in coins:
        for i in range(value, k + 1):
            DP[i] += DP[i - value]
    return DP[-1]


n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

print(coin(k))