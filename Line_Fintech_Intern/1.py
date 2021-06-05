def solution(inputString):
    answer = 0

    # 0~999까지 string을 다 분해해서 넣을 리스트
    strings = []

    # 인덱스로 원래 숫자 찾기 위한 매핑 딕셔너리
    numbers = {}

    # 0~999까지 순회
    for i in range(1000):
        # 시작 인덱스
        start = len(strings)
        # 문자열 리스트 extend
        strings += list(str(i))
        # 끝 인덱스
        end = len(strings)
        # 키: 분해된 문자열 인덱스 / 값: 분해된 값의 원본
        for k in range(start, end):
            numbers[k] = i
    # 각 숫자가 있는지 확인하기 위한 리스트
    valid = [False for _ in range(len(strings))]

    # 남아있는 쿠키 순회를 위한 인덱스 변수
    start = 0
    # 문자열 체킹을 하기 위한 인덱스 변수
    now = 0

    while start < len(inputString) and now < len(strings):
        # 만약 현재 쿠키와 문자열 값이 같다면
        if inputString[start] == strings[now]:
            # 해당 숫자가 있다고 체킹
            valid[now] = True
            # 다음 문자열로
            start += 1
            now += 1
        # 다르다 -> 이미 사라진 쿠키다
        else:
            now += 1
    # stirngs에서 몇번째 인덱스인지 찾기 위한 변수
    result = 0
    # 뒤에서부터 찾기
    for i in range(len(valid) - 1, -1, -1):
        # 만약 처음으로 true인 값이 나왔다 -> 최소의 n 값에서 분해된 문자열 중 하나
        if valid[i]:
            # 해당 문자열 인덱스 저장
            result = i
            break
    # 문자열 인덱스 매핑 테이블을 이용해서 원본 값이 무엇인지 확인
    answer = numbers[result]
    return answer

s = "7234032479947"
assert 47 == solution(s)