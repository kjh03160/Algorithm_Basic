def fib_tab(n):
    temp = [0, 1, 1]    # 고정 값이 담긴 리스트
    for i in range(3, n + 1):  # i는 인덱스
        temp.append(temp[i - 2] + temp[i - 1])  # f(n) = f(n-1) + f(n-2)
    return temp[n]  # f(n) 값 리턴


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))