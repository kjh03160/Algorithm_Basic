# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# O -> 열람햇으나 끝 ㄴ
# W -> 열람 끝 ㅇ
# Y -> 열람 X
mapping = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
score = input().split()
n, m = map(int, input().split())
open_content = [input() for _ in range(n)]
g = [input() for _ in range(n)]

weight = {"Y": 10000, "O": 10}
content = []
for i in range(n):
    for j in range(m):
        if open_content[i][j] == "W":
            continue
        genre = g[i][j]
        original_score = float(score[mapping[genre]])
        weighted_score = weight[open_content[i][j]] * (original_score + 0.01)
        content.append((genre, original_score, weighted_score, (i, j)))

content.sort(key=lambda x: (-x[2], x[3][0], x[3][1]))
for i in content:
    print(i[0], i[1], i[3][0], i[3][1])
