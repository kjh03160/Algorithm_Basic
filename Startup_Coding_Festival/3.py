# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def check(row, col, size, g):
	flag = True
	if row + size > len(G) or col + size > len(G):
		return False
	for r in range(size):
		for c in range(size):
			if not G[row + r][col + c]:
				flag = False
				break
	return flag

def answer(G, black):
	result = [0 for _ in range(n + 1)]

	for i, j in black:
		for size in range(1, n + 1):
			if check(i, j, size, G):
				result[size] += 1
	return result

n = int(input())
G = []
black = set()
for i in range(n):
	x = input()
	temp = []
	for j in range(n):
		if x[j] == "1":
			black.add((i, j))
		temp.append(int(x[j]))
	G.append(temp)

result = answer(G, black)
print("total:", sum(result))
for idx, val in enumerate(result):
	if val:
		print("size[%d]: %d" % (idx, val))