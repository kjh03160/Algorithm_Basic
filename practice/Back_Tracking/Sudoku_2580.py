# https://www.acmicpc.net/problem/2580
import sys

def answer(index):
    global A
    if index == len(A):
        for row in range(9):
            for col in range(9):
                print(L[row][col], end=" ")
            print()
        sys.exit(0) # 답 1개만 출력하기 위해 -> return 하면 답 여러개 출력해버림

    row, col = A[index]
    for number in range(1, 10):
        if check(number, row, col):
            L[row][col] = number
            answer(index + 1)
            L[row][col] = 0


def check(x, row, col):
    square_row = row // 3
    square_col = col // 3
    for i in range(square_row * 3, (square_row + 1) * 3):
        for j in range(square_col * 3, (square_col + 1) * 3):
            if L[i][j] == x:
                return False

    if x not in L[row]:
        for i in range(9):
            if L[i][col] == x:
                return False
        return True

    return False


input = sys.stdin.readline
L = []
A = []
for row in range(9):
    temp = list(map(int, input().split()))
    L.append(temp)
    for col in range(9):
        if temp[col] == 0:
            A.append((row, col))

answer(0)
