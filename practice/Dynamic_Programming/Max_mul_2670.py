# https://www.acmicpc.net/problem/2670

def max_mul(arr):
    DP = [arr[0]]
    for ele in range(1, len(arr)):
        DP.append(max(DP[ele - 1] * arr[ele], arr[ele]))
    print(DP)
    return DP

n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))
print("%.3f" % max(max_mul(arr)))