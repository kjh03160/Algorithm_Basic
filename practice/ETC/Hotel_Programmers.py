# https://programmers.co.kr/learn/courses/30/lessons/64063
import sys
sys.setrecursionlimit(10 ** 6)
def solution(k, room_number):
    answer = []
    room = {}

    for i in room_number:
        answer.append(find_room(room, i))

    return answer

def find_room(room, n):
    # 방이 남아있다면
    if n not in room:
        # 현재 방 다음 번호를 마킹
        room[n] = n + 1
        return n
    # 만약 방이 남아있지 않음 -> 해당 방의 다음 번호 탐색
    x = find_room(room, room[n])
    # 배정된 방 다음 번호 마킹
    room[n] = x + 1
    return x

k = 10
room_number = [1,3,4,1,3,1]
print(solution(k, room_number))