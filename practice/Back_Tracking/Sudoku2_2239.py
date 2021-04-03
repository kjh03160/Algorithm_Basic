# boj.kr/2239

def answer(M, zeros, index):
    if index == len(zeros) - 1:
        for row in M:
            for col in row:
                print(col, end="")
            print()
        sys.exit(0)

    row, col = zeros[index]
    for i in range(1, 10):
        if not is_dup_in_row(M, row, col, i) \
                and not is_dup_in_square(M, row, col, i) \
                    and not is_dup_in_col(M, row, col, i):
            M[row][col] = i
            answer(M, zeros, index + 1)
            M[row][col] = 0


def is_dup_in_row(M, row, col, val):
    for i in range(9):
        if M[row][i] == val:
            return True
    return False

def is_dup_in_col(M, row, col, val):
    for i in range(9):
        if M[i][col] == val:
            return True
    return False


def is_dup_in_square(M, row, col, val):
    r = row // 3
    c = col // 3

    for i in range(r * 3, (r + 1) * 3):
        for j in range(c * 3, (c + 1) * 3):
            if M[i][j] == val:
                return True

    return False


import sys
input = sys.stdin.readline
M = []
zeros = []
for r in range(9):
    x = input().rstrip()
    temp = []
    for c in range(len(x)):
        temp.append(int(x[c]))
        if x[c] == "0":
            zeros.append([r, c])
    M.append(temp)

print(answer(M, zeros, 0))

