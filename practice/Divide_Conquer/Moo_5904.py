# 5904

def length(n):
    result = 0
    for i in range(1, 29):
        result = result + i + 2 + result
        if result >= n:
            return result, i

def answer(n, k = 1):
    text = 'moo'
    if k == 0:
        return text[n - 1]

    l, k = length(n)

    middle = k + 2
    left = (l - middle) // 2
    middle = left + middle

    if n <= left:
        return answer(n, k - 1)
    elif n > middle:
        return answer(n - middle, k - 1)

    text = 'm' + 'o' * (k + 1)
    n -= left

    return text [n - 1]

N = int(input())
print(answer(N))
