# 1780
def verify(matrix):
    std = matrix[0][0]
    for i in matrix:
        for j in i:
            if std != j:
                return False
    return True

def answer(matrix):
    global color

    v = verify(matrix)
    if v:
        color[matrix[0][0]] += 1
        return

    divide = len(matrix) // 3
    for i in range(0, len(matrix), divide):
        for j in range(0, len(matrix), divide):
            answer([k[j : j + divide] for k in matrix[i : i + divide]])

n = int(input())
matrix = [list(map(int, input().split())) for i in range(n)]
color = [0, 0, 0]
answer(matrix)
print(color[-1], color[0], color[1],  sep='\n')