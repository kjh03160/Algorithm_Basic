def course_selection(course_list):
    # 수업 시작을 기준으로 정렬
    course_list.sort()
    # 수업 개수 비교를 위한 변수
    count = 0
    # 가장 많이 들을 수 있는 경우 수업 리스트
    result = []

    for i in range(len(course_list)):
        # i 번째 수업을 담기
        course = [course_list[i]]
        # i + 1 번째 수업을 담겨진 수업과 비교하며 가능한 수업 담기
        for j in range(i, len(course_list)):
            if course_list[j][0] <= course[-1][1]:
                continue
            course.append(course_list[j])
            count += 1
        # 담겨진 수업이 현재 가장 많이 담긴 것보다 크면 바꾸기
        if len(course) > len(result):
            result = course
    return result


def course_selection_sorting(course_list):
    # 수업을 끝나는 순서로 정렬한다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# 테스트
print(course_selection_sorting([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection_sorting([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection_sorting([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
