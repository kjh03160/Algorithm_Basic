def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(f(num))
    return answer

def f(num):
    result = 1
    for i in range(num + 1, (num << 1) + 1):
        val = i ^ num
        if val >= 1:
            count = 0
            while val > 0:
                if val & 1:
                    count += 1
                if count > 2:
                    break
                val = val >> 1
            if i ^ num and count <= 2:
                result = i
                break
    return result

import math
def f2(num):
    if num == 0:
        return 1
    length = int(math.log2(num))
    if num == 2 ** (length + 1) - 1:
        return num + 2 ** length
    if num < 8:
        return num + 1

    tmp = (2 ** (length + 1) - 1 - num)
    if tmp % 4:
        return num + 1

    plus_count = 2 ** (length - 2) + 1
    index = (tmp // 4) - 1
    if index % 2 == 0:
        return num + 2

    if index - 1 % 4 == 0:
        return num + 4

    mid = plus_count // 2

    if index == mid:
        return 2 ** mid + num
    if index > mid:
        x = mid - index
        index = mid - x




print([i for i in range(129)])
print(solution([i for i in range(129)]))
print(f2(7))
print(bin(19))
print(0b10101)

"""
1 -> 2   1

3 -> 5   2

7 -> 11  4

3
11 -> 13 2
15 -> 23 8 1

4
19 -> 21 2
23 -> 27 4
27 -> 29 2
31 -> 47 16 3

35 -> 37 2
39 -> 43 4
43 -> 45 2
47 -> 55 8
51 -> 53 2
55 -> 59 4
59 -> 61 2
63 -> 95 32 7

67 -> 69 2
71 -> 75 4
75 -> 77 2
79 -> 87 8
83 -> 85 2
87 -> 91 4
91 -> 93 2
95 -> 111 16
99 -> 101 2
103 -> 107 4 15
"""
"""
1 3 7 15 
"""