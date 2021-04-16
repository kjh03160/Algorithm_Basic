# boj.kr/19598

import heapq
def answer(L):
    L.sort()
    result = 0
    count = 0
    for i in L:
        count += i[1]
        result = max(result, count)
    return result

def answer2(L):
    L.sort()
    # 끝 값 넣기
    # 빨리 끝나는 순으로 정렬
    q = [L[0][1]]
    for i in range(1, n):
        # 시작 시간이 현재 회의 시간 이후 라면
        if L[i][0] >= q[0]:
            # 앞선 회의가 끝났다.
            # 회의실을 추가 안해도 된다.
            heapq.heappop(q)
        # 새로운 회의를 시작한다.
        heapq.heappush(q, L[i][1])
    return len(q)

import sys
input = sys.stdin.readline
n = int(input().rstrip())
L = []
Q = []
for _ in range(n):
    a, b = map(int, input().split())
    L.append([a, 1])
    L.append([b, -1])
    Q.append([a, b])

print(answer(L))
print(answer2(Q))