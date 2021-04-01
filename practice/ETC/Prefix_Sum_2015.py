# boj.kr/2015

def answer(L, k):
    count = {0: 1}
    c = 0
    # psum[i] - psum[j-1] = k인 횟수를 구해야된다.
    # 하지만 이 방법은 n^2 -> 값들이 0, 음수가 포함되어 있기에 투포인터로는 안됨
    # psum[i] - k = psum[j-1]임.
    # k값을 기준으로 저장하려고 하면 21억이여서 메모리 초과.
    # 부분합 값들을 미리 저장 -> 20만이여서 가능.
    # 해당 값이 나올때마다 횟수를 더해주자.

    for i in range(len(L) - 1):
        L[i] += L[i - 1]
        if L[i] - k in count:
            c += count[L[i] - k]
        if L[i] in count:
            count[L[i]] += 1
        else:
            count[L[i]] = 1
    return c

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
L = list(map(int, input().split()))
L.append(0)
print(answer(L, k))