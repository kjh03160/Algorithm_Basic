"""
규식이는 친구들 사이에서 투자의 귀재로 알려져 있습니다. 페이수북과 인수타그램에 자신의 성과를 과시하기 때문인데요. 사실 규식이가 그 정도의 실력자는 아닙니다. 성과가 좋을 때에만 SNS에 공유해서 그렇게 비춰질 뿐이죠.

계속해서 멋진 모습을 보여주기 위해, 특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수 sublist_max를 작성해 보려고 합니다.
"""
def sublist_max(profits):
    max = 0
    for start in range(len(profits)):
        for end in range(len(profits), -1, -1):
            val = sum(profits[start:end])
            if max < val:
                max = val
    return max

# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))