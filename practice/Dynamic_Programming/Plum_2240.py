# https://www.acmicpc.net/problem/2240

def plum(arr, w):
    dp = [[0 for count in range(w + 1)] for time in range(len(arr) + 1)]
    count = 0
    for time in range(len(arr)):
        for count in range(w + 1):
            if count == 0:
                if arr[time] == 1:
                    dp[time][count] = dp[time - 1][count] + 1
                else:
                    dp[time][count] = dp[time - 1][count]
                continue

            if count % 2 == 0:   # 짝수 번 움직이면 나무 1
                if arr[time] == 1:
                    dp[time][count] = max(dp[time - 1][count - 1], dp[time - 1][count]  + 1)
                else:
                    dp[time][count] = max(dp[time - 1][count - 1] + 1, dp[time - 1][count])

            else:
                if arr[time] == 1:
                    dp[time][count] = max(dp[time - 1][count - 1] + 1, dp[time - 1][count])
                else:
                    dp[time][count] = max(dp[time - 1][count - 1], dp[time - 1][count] + 1)

    answer = 0
    for i in range(w + 1):
        answer = max(answer, dp[len(arr) - 1][i])
    # for i in dp:
    #     print(i)
    return answer


n, w = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

print(plum(arr, w))

t, w = map(int, input().split())
a = [0]
dp = [[0] * (w + 1) for _ in range(t + 1)]

for _ in range(t):
    a.append(int(input()))

if a[1] == 1:
    dp[1][0] = 1
    dp[1][1] = 0
else:
    dp[1][0] = 0
    dp[1][1] = 1

for x in range(2, t + 1):
    if a[x] == 1:
        dp[x][0] = dp[x - 1][0] + 1
    else:
        dp[x][0] = dp[x - 1][0]

    for y in range(1, w + 1):
        dp[x][y] = max(dp[x - 1][y - 1], dp[x - 1][y])

        if y % 2 + 1 == a[x]:
            dp[x][y] += 1

print(max(dp[t]))