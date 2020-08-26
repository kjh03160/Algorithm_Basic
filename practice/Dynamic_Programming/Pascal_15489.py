# 15489

R, C, W = map(int, input().split())

tri = [[]]
for i in range(1, R + W):
    temp = [1 for _ in range(i)]
    for j in range(1, i - 1):
        temp[j] = tri[i - 1][j - 1] + tri[i - 1][j]
    tri.append(temp)

result = 0
for i in range(1, W + 1):
    result += sum(tri[i + R - 1][C - 1 : i + C - 1])

print(result)