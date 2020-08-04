def fibo_rec(n):
    if n < 1:
        return 1
    return fibo_rec(n - 1) + fibo_rec(n - 2)

def fibo_array(n):
    array = [0, 1]
    for i in range(2, n + 1):
        array.append(array[i - 1] + array[i - 2])
    return array[n]

def fibo_three(n):
    prev = 0
    current = 1
    for i in range(2, n + 1):
        temp = prev + current
        prev = current
        current = temp
    return current

def fibo_pow(n):
    SIZE = 2
    ZERO = [[1, 0], [0, 1]] # 행렬의 항등원
    BASE = [[1, 1], [1, 0]] # 곱셈을 시작해 나갈 기본 행렬

    # 두 행렬의 곱을 구한다
    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]

        return new

    # 기본 행렬을 n번 곱한 행렬을 만든다
    def get_nth(n):
        matrix = ZERO[:]
        tmp = BASE[:]

        if n == 0:
            return matrix

        x = get_nth(n // 2)

        if n % 2 == 0:
            return square_matrix_mul(x, x)  # x * x
        return square_matrix_mul(square_matrix_mul(x, x), tmp)  # x * x * a

    return get_nth(n)[1][0]

print(fibo_pow(10))