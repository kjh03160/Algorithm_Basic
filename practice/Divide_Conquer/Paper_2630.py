# 2630
def verify(matrix):
    result = 2
    temp = 0
    for i in matrix:
        temp += sum(i)
    if temp == len(matrix) ** 2:
        result = 1
    elif temp == 0:
        result = 0
    return result

def answer(matrix):
    global color
    if len(matrix) <= 1:
        color[matrix[0][0]] += 1
        return

    v = verify(matrix)
    if v != 2:
        color[v] += 1
        return

    mid = len(matrix) // 2
    a = [i[:mid] for i in matrix[:mid]]
    b = [i[:mid] for i in matrix[mid:]]
    c = [i[mid:] for i in matrix[:mid]]
    d = [i[mid:] for i in matrix[mid:]]

    answer(a)
    answer(b)
    answer(c)
    answer(d)

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
color = [0, 0]
answer(matrix)
print(color[0], color[1], sep='\n')