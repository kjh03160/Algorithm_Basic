# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    min_dist = 9999999999
    min_st1 = None
    min_st2 = None
    length = len(coordinates)

    for i in range(length):
        st1 = coordinates[i]
        for j in range(i + 1, length):
            st2 = coordinates[j]
            dist = distance(st1, st2)
            if min_dist > dist:
                min_dist = dist
                min_st1 = st1
                min_st2 = st2
    return [min_st1, min_st2]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))