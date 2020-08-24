# 14697

x = input().split()
n = int(x[-1])
k = list(map(int, x[:3]))

def answer(n, k):
    DP = [0 for i in range(301)]
    for i in k:
        DP[i] = 1

    for i in range(1, n + 1):
        if DP[i] or DP[i - k[0]] or DP[i - k[1]] or DP[i - k[2]]:
            DP[i] = 1
    return DP[n]

print(answer(n, k))