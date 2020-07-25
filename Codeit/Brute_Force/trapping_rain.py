"""
강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.

그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.

함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.

예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다. 그러면 0번 인덱스에 높이 33의 건물이, 3번 인덱스에 높이 22의 건물이, 5번 인덱스에 높이 44의 건물이 있다는 뜻입니다. 1번, 2번, 4번 인덱스에는 건물이 없습니다.
"""


def trapping_rain(buildings):
    result = 0
    length = len(buildings)
    for i in range(1, length - 1):
        now = buildings[i]
        left_height = 0
        right_height = 0

        # 왼쪽 가장 큰 건물 찾기
        for left in range(i):
            if buildings[left] > left_height:
                left_height = buildings[left]

        # 오른쪽 가장 큰 건물 찾기
        for right in range(i + 1, length):
            if buildings[right] > right_height:
                right_height = buildings[right]

        # 더 낮은 건물 찾기
        standard = left_height
        if standard > right_height:
            standard = right_height

        rains = standard - now
        # 현재 건물보다 큰 건물로 둘러싸여 있지 않을 경우
        if rains < 0:
            continue

        result += rains
    return result


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))