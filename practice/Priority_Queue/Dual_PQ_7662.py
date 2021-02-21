# https://www.acmicpc.net/problem/7662


import heapq

def answer(L):
    min_heap = []
    max_heap = []
    poped = [False for i in range(len(L))]

    for i in range(len(L)):
        command, num = L[i]
        if command == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
        elif command == "D":
            if num == 1:
                # 힙이 비거나, 최대 힙에 있는 최대 힙이 안지워진 숫자일 때까지 pop
                while True:
                    if not len(max_heap) or not poped[max_heap[0][1]]:
                        break
                    heapq.heappop(max_heap)

                # 힙이 남아있다 -> 빼낼 최댓값이 있다.
                if max_heap:
                    # 삭제 후, 배열에 지워졌다고 체크
                    out = heapq.heappop(max_heap)
                    poped[out[1]] = True
            else:
                while True:
                    if not len(min_heap) or not poped[min_heap[0][1]]:
                        break
                    heapq.heappop(min_heap)
                if min_heap:
                    out = heapq.heappop(min_heap)
                    poped[out[1]] = True

    # 모든 연산 후에 최신화 되지 않은(이미 삭제된) 값들이 반대의 힙에 있다면 pop
    while max_heap and poped[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and poped[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if len(min_heap) and len(max_heap):
        return "%d %d" % (-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
    return "EMPTY"


import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    L = []
    for _ in range(int(input())):
        x = input().split()
        x[1] = int(x[1])
        L.append(x)
    print(answer(L))