# https://www.acmicpc.net/problem/14916

n = int(input())

DP = [200001]
for five in range((n // 5) + 1):
    remain = n - five * 5
    two = remain // 2
    if remain - (two * 2) == 0:
        DP.append(min(DP[-1], two + five))

if len(DP) > 1:
    print(DP[-1])
else:
    print(-1)
