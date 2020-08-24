# S는 수업 시작 시간
# F는 수업 끝나는 시간
# L은 강의 번호
# 가장 빨리 끝나는 강의부터 선택

def Greedy(S, F):
    L = [0]
    k = 0
    for i in range(1, len(S)):
        if S[i] >= F[k]:
            L.append(i)
            k = i
    return L

S = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
F = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print(Greedy(S, F))