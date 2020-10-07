# https://www.acmicpc.net/problem/2156

def wine(arr):
    DP = [0] * len(arr)
    DP[0] = arr[0]
    if len(arr) > 1:
        DP[1] = arr[0] + arr[1]
    for i in range(2, len(arr)):
        a = DP[i - 2] + arr[i]   # 1번 연속 마시는 경우
        b = DP[i - 3] + arr[i - 1] + arr[i] # 2번 연속 마시는 경우
        c = DP[i - 1]   # 0번 연속 마시는 경우
        DP[i] = max(a, b, c)
    return DP[-1]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(wine(arr))