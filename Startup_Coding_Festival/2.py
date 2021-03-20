# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
K = input()
DP = [0 for _ in range(n)]
DP[0] = 1
for i in range(1, n):
	if K[i] == "0":
		continue
	DP[i] = DP[i -1] + DP[i - 2]

print(DP[-1])