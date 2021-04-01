# boj.kr/10986


from itertools import combinations
def answer(L, m):
    count = [0 for _ in range(m)]
    s = 0
    # 부분 합을 모듈러 연산하여 나머지 값들의 개수를 구한다.
    for i in range(len(L)):
        s += L[i]
        count[s % m] += 1

    # 자기 자신이 0인 것 포함하기 위해
    ans = count[0]

    # 부분합의 개수 C 2
    # 만약 나머지가 1인 것이 2개 이상이다? -> 그 사이에 m으로 나누어 떨어지는 부분 수열이 존재한다.
    # 그러므로 모든 나머지 값들에 대해 도는 것!
    for i in range(m):
        # print(((count[i] * (count[i] - 1)) // 2))
        ans += ((count[i] * (count[i] - 1)) // 2)
    return ans


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L = list(map(int, input().split()))
print(answer(L, m))

