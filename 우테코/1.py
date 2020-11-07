def solution(grades, weights, threshold):
    answer = -1234567890
    # 매핑 딕셔너리
    mapping_t = {"A+" : 10, "A0" : 9, "B+" : 8, "B0" : 7,
                "C+" : 6, "C0" : 5, "D+" : 4, "D0" : 3, "F" : 0}
    # 가중치 점수 합
    temp = 0
    for i in range(len(grades)):
        grade = mapping_t[grades[i]]
        weight = weights[i]
        score = grade * weight
        temp += score
    answer = temp - threshold
    return answer