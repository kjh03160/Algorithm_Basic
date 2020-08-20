def LCS(X, Y):
    matrix = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]

    def leng(n, m):
        if n == 0 or m == 0:
            return 0
        if X[n - 1] == Y[m - 1]:
            return leng(n - 1, m - 1) + 1
        else:
            return max(leng(n - 1, m), leng(n, m - 1))

    for i in range(len(X) + 1):
        for j in range(len(Y) + 1):
            matrix[i][j] = leng(i, j)

    return matrix[len(X)][len(Y)]


X = "ABCBDAB"
Y = "BDCABA"

print(LCS(X, Y))