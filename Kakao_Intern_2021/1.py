def solution(s):
    answer = ''
    mapping = {'zero': 0, 'one': 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    temp = ''
    for string in s:
        if string.isdigit():
            answer += string
        else:
            temp += string
        if temp in mapping:
            answer += str(mapping[temp])
            temp =''
    answer = int(answer)
    return answer

s = "one4seveneight"
print(solution(s))