# boj.kr/1339

def anwser(N):
    N.sort(key=lambda x: len(x), reverse=True)

    temp = {}
    for i in N:
        for char in range(len(i)):
            if i[char] not in temp:
                temp[i[char]] = 0
            temp[i[char]] += 10 ** (len(i) - char - 1)

    start = 9
    for char, val in sorted(list(temp.items()), key=lambda x: -x[1]):
        temp[char] = start
        start -= 1

    result = 0
    for i in N:
        st = ''
        for string in i:
            st += str(temp[string])
        result += int(st)
    return result


import sys
input = sys.stdin.readline
n = int(input())
N = []
cand = set()
for i in range(n):
    x = input().rstrip()
    N.append(x)
print(anwser(N))