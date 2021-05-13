import math
def solution(left, right):
    answer = 0

    for num in range(left, right + 1):
        l = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                l += 1
                if i ** 2 < num:
                    l += 1
        if l % 2:
            answer -= num
        else:
            answer += num

    return answer


print(solution(13, 17))