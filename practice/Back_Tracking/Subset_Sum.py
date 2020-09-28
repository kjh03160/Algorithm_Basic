def subset1(A, S):
    if S == 0:
        return True
    elif S < 0 or len(A) == 0:
        return False

    for i in range(len(A) - 1, - 1, -1):
        z = A[i]
        with_z = subset1(A[:i], S - z)
        out_z = subset1(A[:i], S)
        return with_z or out_z

def subset(k, total):
    global n, A, S, ans
    if k >= n:
        return False

    total += A[k]
    if total == S:
        ans += 1
    subset(k + 1, total)
    subset(k + 1, total - A[k])


ans = 0
n, S = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
# for i in range(n):
#     x = [0 for i in range(n)]
#     subset(i)
subset(0, 0)
print(ans)