"""
Tabulation 방법
- bottom up으로 가기에 공간 복잡도 O(n)

하지만 메모리를 더 최적화 할 수 있다.
prev, current 두 개의 변수만 사용해서 O(1) 가능
"""

def fib_optimized(n):
    prev = 0
    current = 1
    # [1, 1]
    if n < 2:
        return current
    for i in range(1, n):   # 반복문을 돌면서 n까지 값을 더해감
        prev, current = current, current + prev
    return current


# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
