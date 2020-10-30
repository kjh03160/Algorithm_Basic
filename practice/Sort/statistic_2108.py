#  https://www.acmicpc.net/problem/2108


def answer(num_list):
    mean = 0
    medain = 0
    mode = 0
    ran = 0

    count_dict = {}
    num_list.sort()

    for i in range(len(num_list)):
        mean += num_list[i]
        if num_list[i] not in count_dict.keys():
            count_dict[num_list[i]] = 1
        else:
            count_dict[num_list[i]] += 1

    mean = int(round(mean / len(num_list), 0))
    medain = num_list[len(num_list) // 2]
    count_dict = list(count_dict.items())
    count_dict.sort(key = lambda x : x[1], reverse=True)
    if len(count_dict) > 1 and count_dict[0][1] == count_dict[1][1]:
        mode = count_dict[1][0]
    else:
        mode = count_dict[0][0]

    if num_list[0] * num_list[-1] < 0:
        ran = abs(num_list[0]) + abs(num_list[-1])
    else:
        ran = abs(num_list[0] - num_list[-1])

    return mean, medain, mode, ran


import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

print(*answer(numbers), sep = '\n')


# -------------------------------------------
count = [0] * 8001
N = int(input())
for i in range(N):
    a = int(input())
    count[a + 4000] += 1

math_mean = int(round(sum([count[i] * (i - 4000) for i in range(len(count))]) / N, 0))

if N % 2 == 1:
    temp_sum = 0
    for i in range(len(count)):
        temp_sum += count[i]
        if temp_sum >= ((N // 2) + 1):
            median = i - 4000
            break
else:
    temp_sum = 0
    for i in range(len(count)):
        temp_sum += count[i]
        if temp_sum >= (N // 2):
            median_1 = i - 4000
    temp_sum = 0
    for i in range(len(count)):
        temp_sum += count[i]
        if temp_sum >= ((N // 2) + 1):
            median_2 = i - 4000
    median = int(round((median_1 + median_2) / 2, 0))

max_count = max(count)
max_ix = count.index(max_count)
if max_count in count[(max_ix + 1):]:
    mode = count.index(max_count, max_ix + 1, len(count)) - 4000
else: mode = max_ix - 4000

temp_range = [i - 4000 for i in range(len(count)) if count[i]!=0]
range_c = max(temp_range) - min(temp_range)

print(math_mean)
print(median)
print(mode)
print(range_c)