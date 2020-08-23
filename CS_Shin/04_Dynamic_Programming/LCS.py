def LCS(X, Y):
    matrix = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]

    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    string = ""
    def LCS_string(n, m, string):
        if n == 0 or m == 0:
            return string

        if X[n - 1] == Y[m - 1]:
            string = X[n - 1] + string
            return LCS_string(n - 1, m - 1, string)

        if matrix[n - 1][m] > matrix[n][m - 1]:
            return LCS_string(n - 1, m, string)
        return LCS_string(n, m - 1, string)

    string = LCS_string(len(X), len(Y), string)


    return matrix[len(X)][len(Y)], string


X = input()
Y = input()

print(LCS(X, Y))