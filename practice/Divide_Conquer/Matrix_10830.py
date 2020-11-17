# https://www.acmicpc.net/problem/10830

def make_matrix(A, matrix):
    dummy_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                dummy_matrix[i][j] += (matrix[i][k] * A[k][j])
            dummy_matrix[i][j] %= 1000

    return dummy_matrix


def answer(A, B):
    if (B == 1):
        return A

    # 홀수, A를 마지막에 곱
    # AAAAA -> (A^2)^2 * A
    elif ((B % 2) == 1):
        matrix = answer(A, B - 1)
        new_matrix = make_matrix(A, matrix)

        return new_matrix

    # 짝수, 제곱수로 계속
    # AAAA -> (A^2) = AA -> (A^2)^2 = AAAA
    else:
        matrix = answer(A, B // 2)
        new_matrix = make_matrix(matrix, matrix)
        return new_matrix


import sys
input = sys.stdin.readline
n, b = map(int, input().split())
m = [tuple(map(int, input().strip().split())) for _ in range(n)]

result = answer(m, b)
for i in range(len(result)):
    for j in range(len(result)):
        print(result[i][j] % 1000, end=" ")
    print()