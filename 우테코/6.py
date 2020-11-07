def solution(logs):
    answer = []

    # 학생 사전
    students = {}
    # {수험생 : {문제 : 점수}, ...} 형식
    for i in logs:
        string = i.split()
        std = string[0]
        number = int(string[1])
        score = string[2]

        # 수험생이 이미 있다면
        if std not in students.keys():
            students[std] = {number: int(score)}
        else:
            students[std][number] = int(score)

    # 수험생 번호 추출
    student_list = list(students.keys())

    for a in range(len(student_list)):
        student_a = student_list[a]  # A 수험생 번호

        # A학생의 (문제, 점수) 형식으로 추출, 문제 번호순으로 정렬
        a_numbers = sorted(list(students[student_a].items()))

        if len(a_numbers) < 5:  # 푼 문제가 5문제 미만이라면 확인할 필요 없음
            continue

        for b in range(a + 1, len(student_list)):
            is_cheat = True  # A와 비교할 학생이 부정행위자인지 확인할 불린 값
            student_b = student_list[b]  # B 수험생 번호

            # B학생의 (문제, 점수) 형식으로 추출, 문제 번호순으로 정렬
            b_numbers = sorted(list(students[student_b].items()))

            # B 학생이 문제를 5개 미만 or 푼 문제수가 다를 경우 확인할 필요 없음
            if len(b_numbers) < 5 or len(b_numbers) != len(a_numbers):
                continue

            # A와 B의 푼 문제 및 점수 비교
            for pb in range(len(b_numbers)):
                pb_a_score = a_numbers[pb][1]  # A가 푼 문제 점수
                pb_a_number = a_numbers[pb][0]  # A가 푼 문제 번호
                pb_b_score = b_numbers[pb][1]  # B가 푼 문제 점수
                pb_b_number = b_numbers[pb][0]  # B가 푼 문제 번호
                # 서로 다른 문제를 풀었거나, 점수가 다르면 부정행위 X, 더이상 볼 필요 없음
                if pb_b_number != pb_a_number or pb_a_score != pb_b_score:
                    is_cheat = False
                    break
            # 모두 검사했을때,  is_cheat이 True라면 부정행위자
            if is_cheat:
                answer.extend([student_b, student_a])
    # 아무도 부정행위를 안했을 때
    if len(answer) == 0:
        answer.append("None")
    # 중복 제거 및 사전형 정렬
    answer = sorted(list(set(answer)))

    return answer