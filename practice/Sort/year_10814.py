# https://www.acmicpc.net/problem/10814

def answer(years):
    years.sort(key=lambda x : x[0])
    pass

import sys
input = sys.stdin.readline

n = int(input())
years = []

for _ in range(n):
    year, name = input().split()
    years.append([int(year), name])
answer(years)
for year, name in years:
    print(year, name)

# 최대 input 개수만큼 리스트 생성
# 들어오는 나이를 인덱스로 삼고 해당 행에 데이터 삽입
# 순서대로 출력
from sys import stdin, stdout

users_by_age = [[] for _ in range(200+1)]

for line in stdin.read().splitlines(True)[1:]:
    users_by_age[int(line.split()[0])].append(line)

stdout.write(''.join(
    ''.join(u)
    for u in
    users_by_age
))