def N_Queens(k, N):
    global x, result
    if k == N:
        result += 1
        print("result : " , x)
    else:
        for i in range(N):
            if B(k, i) == True:
                x[k] = i
                N_Queens(k + 1, N)



def B(k, c):    # Queen을 k행 c열에 놓을 수 있는가?
    for i in range(k):
        if c == x[i] or abs(c - x[i]) == k - i: # 같은 열에 이미 놓여져 있거나, 대각선으로 연결되어 있거나
            return False
    return True

result = 0
x = [0 for i in range(4)]
N_Queens(0, 4)
print(result)
