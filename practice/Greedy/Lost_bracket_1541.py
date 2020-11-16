# https://www.acmicpc.net/problem/1541
#  50-60+60+70+70-50
def answer(data):
    k = []
    if len(data) == 1:
        return data[0]
    temp_list = []
    for i in range(len(data)):
        if data[i] == "-":
            k.append(sum(temp_list))
            k.append(data[i])
            temp_list.clear()
        elif data[i] == "+":
            pass
        else:
            temp_list.append(data[i])
    k.append(sum(temp_list))

    result = k[0]
    for i in range(1, len(k)):
        if k[i] != "-":
            result = result - k[i]
    return result

import sys
input = sys.stdin.readline

string = input().strip()
numbers = []
ops = []
temp = ''
for s in range(len(string)):
    if string[s].isdigit():
        temp += string[s]
        if s == len(string) - 1:
            numbers.append(int(temp))
    else:
        numbers.append(int(temp))
        numbers.append(string[s])
        temp = ''
print(answer(numbers))


#########################################################
# 다른 사람 코드
exp = input()
result = 0

# 뺄셈 기준으로 나눠준다.
subtractions = exp.split("-")

for sub in range(len(subtractions)):
    addition = list(map(int, subtractions[sub].split("+")))
    temp = sum(addition)
    if sub == 0:
        result += temp
    else:
        result -= temp

print(result)
##############################################################