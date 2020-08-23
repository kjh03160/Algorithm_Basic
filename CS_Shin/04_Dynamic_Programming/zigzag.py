# n = int(input())
# x = list(map(int, input().split()))

x = [1, 1, 1, 2, 2, 3]
n = len(x)

high = [1 for i in range(n)]
low = [1 for i in range(n)]

# 비연속 부분 수열
for k in range(n):
    for j in range(k):
        if x[j] < x[k]:
            val = max(high[k], low[j] + 1)
            if val == high[k]:
                break
            high[k] = max(high[k], low[j] + 1)
        if x[j] > x[k]:
            val = max(low[k], high[j] + 1)
            if val == low[k]:
                break
            low[k] = max(low[k], high[j] + 1)

# 연속된 부분수열
for k in range(1, n):
    if x[k - 1] < x[k]:
        high[k] = max(high[k], low[k - 1] + 1)
    if x[k - 1] > x[k]:
        low[k] = max(low[k], high[k - 1] + 1)


max_val = 0
for k in range(n):
    max_val = max(max_val, max(low[k], high[k]))

print(max_val)