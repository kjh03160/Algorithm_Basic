# Success

import math
from  collections import defaultdict
def solution(fees, records):
    answer = []

    default_time = fees[0]
    default_fee = fees[1]
    time = fees[2]
    fee = fees[3]

    cars = dict()
    total_times = defaultdict(int)

    # 시각, 차량번호, 내역
    for i in range(len(records)):
        t, car_num, text = records[i].split()
        t_ = list(map(int, t.split(":")))
        minutes = t_[0] * 60 + t_[1]
        if text == "IN":
            cars[car_num] = minutes
        else:
            total_times[car_num] += minutes - cars[car_num]
            cars[car_num] = -1
    car_keys = sorted(list(cars.keys()))
    last_time = 23 * 60 + 59
    for car in car_keys:
        if cars[car] != -1:
            total_times[car] += last_time - cars[car]
            cars[car] = -1

        answer.append(fee_sum(total_times[car], default_fee, default_time, time, fee))

    return answer

def fee_sum(total, default_fee, default_time, time, fee):
    if total <= default_time:
        return default_fee
    else:
        return default_fee + math.ceil((total - default_time) / time) * fee

print(solution(	[1, 461, 1, 10], ["00:00 1234 IN"]))