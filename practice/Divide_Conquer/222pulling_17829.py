# 17829

def answer(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    result_matrix = [[] for i in range(len(matrix) // 2)]
    row = 0
    for i in range(0, len(matrix), 2):
        col = 0
        second = 10001
        for j in range(0, len(matrix), 2):
            temp = [x[j :j + 2] for x in matrix[i : i + 2]]
            temp[0].sort(reverse=True)
            temp[1].sort(reverse=True)
            # print(temp)
            if temp[0][0] > temp[1][0]:
                if temp[0][1] > temp[1][0]:
                    second = temp[0][1]
                else:
                    second = temp[1][0]
            else:
                if temp[0][0] > temp[1][1]:
                    second = temp[0][0]
                else:
                    second = temp[1][1]

            result_matrix[row].append(second)
            col += 1
        row += 1
    # print(result_matrix)


    return answer(result_matrix)


N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

print(answer(matrix))