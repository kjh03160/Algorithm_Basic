"""
임의의 k번째 작은 수 찾기

Quick Select 알고리즘
1. 임의의 수를 하나 선택 -> 피벗
2. 피벗과 나머지 수를 비교하여 작은 수, 같은 수, 큰 수 분리
3. 작은 수의 개수가 k개와 같거나 작다면 작은 수 부분에 찾는 값이 있다.
4. 작은 수의 개수와 같은 수의 개수가 k보다 작다면 큰 수 부분에 값이 있다.
5. 둘 다 아니라면 피벗 값이 k번째로 작은 수다.
"""

def quickselect(L, k):
    pivot = L[0]
    left, mid, right = [], [], []
    mid.append(pivot)
    for i in range(1, len(L)):
        if L[i] < pivot:
            left.append(L[i])
        elif L[i] > pivot:
            right.append(L[i])
        else:
            mid.append(L[i])
    if len(left) >= k:
        return quickselect(left, k)
    elif len(left) + len(mid) < k:
        return quickselect(right, k - len(left) - len(mid))
    else:
        return pivot


n, k = map(int, input().split())    # 입력 수의 개수, k번째로 작은 수

L = list(map(int, input().split())) # 입력 수 리스트

print(quickselect(L, k))
