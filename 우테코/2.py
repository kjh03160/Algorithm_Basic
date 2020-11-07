def solution(s, op):
    answer = []

    for i in range(len(s) - 1):  # i 길이만큼 슬라이싱
        first = int(s[:i + 1])  # 앞 숫자
        second = int(s[i + 1:])  # 뒷 숫자
        # 연산
        if op == "+":
            answer.append(first + second)
        elif op == "-":
            answer.append(first - second)
        else:
            answer.append(first * second)
    return answer