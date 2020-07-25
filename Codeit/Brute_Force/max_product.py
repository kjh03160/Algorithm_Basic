"""
Brute Force
- 모든 경우의 수를 탐색
장점
1. 직관적이고, 명확
2. 답을 확실하게 찾을 수 있음.
단점
1. 인풋이 엄청 커지는 경우엔 비효율적
"""
def max_product(left_cards, right_cards):
    max = -9999999999
    for i in left_cards:
        for j in right_cards:
            if i * j > max:
                max = i * j
    return max


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))