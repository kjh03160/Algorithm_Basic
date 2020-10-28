# https://www.acmicpc.net/problem/7568

def answer(n, l):
    rank_list = []
    for i in range(n):
        rank = 1
        for j in range(n):
            if l[i][0] < l[j][0] and l[i][1] < l[j][1]:
                rank += 1
        rank_list.append(str(rank))

    return " ".join(rank_list)



n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

print(answer(n, l))