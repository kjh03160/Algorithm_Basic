#  9625

k = int(input())

DP = [(1, 0)]
for i in range(k):
    temp = DP[i][0]
    b = DP[i][1]
    a = DP[i][1]
    b += temp
    DP.append((a, b))

print(DP[k][0], DP[k][1])