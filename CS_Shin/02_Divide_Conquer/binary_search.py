def binary_search(A, i, j, x):
    if i > j:   # 탐색 범위 내에 없다
        return None

    m = (i + j) // 2    # 중간 인덱스
    if x == A[m]:   # x 발견
        return m
    elif x < A[m]:  # 왼쪽 반 탐색
        return binary_search(A, i, m - 1, x)
    else:           # 오른쪽 반 탐색
        return binary_search(A, m + 1, j, x)


A = [2 * i for i in range(11)]  # A = [0, 2, 4, ..., 20]
print(A)
while True:  # x = -1을 입력받을 때까지 반복
    x = int(input("x = "))
    if x == -1: break
    index = binary_search(A, 0, 19, x)
    if index == -1:
        print("Not found!")
    else:
        print(str(x) + " is found at index " + str(index))
print("END")