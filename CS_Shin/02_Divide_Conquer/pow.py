def power1(a, n):
    """선형 재귀 호출 O(n)"""
    if n == 1:
        return a
    return a * power1(a, n - 1)


def power2(a, n):
    """이진 재귀 호출 O(log n)"""
    if n == 1:
        return a
    if n == 0:
        return 1
    if n % 2 == 0:
        return power2(a, n // 2) * power2(a, n // 2)
    return power2(a, n // 2) * power2(a, n // 2) * a


def power3(a, n):
    """더 빠른 이진 재귀 호출 O(log n)"""
    if n == 0:
        return 1
    x = power3(a, n // 2)
    if n % 2 == 0:
        return x * x
    return x * x * a