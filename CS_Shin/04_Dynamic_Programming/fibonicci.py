def fibo_recur(n):
    if n <= 1:
        return n
    else:
        return fibo_recur(n - 1) + fibo_recur(n -2)

memo = dict()
def fibo_memo(n):
    if n in memo.keys():
        return memo[n]
    f = None
    if n <= 1:
        f = 1
    else:
        f = memo[n - 1] + memo[n - 2]
    memo[n] = f
    return f

def fibo_tab(n):
    L = [0, 1]
    for i in range(2, n + 1):
        L.append(L[n - 1] + L[n - 2])
    return L[n]