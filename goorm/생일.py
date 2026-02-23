# 입력 : 학생 수, 생일
# 나이가 많은 순서대로, 적은 순서대로 정렬할 수 있는 리스트 생성
# 출력 : 가장 나이가 적은 사람과 많은 사람 출력

import sys
input = sys.stdin.readline

n = int(input())
arr1 = []
arr2 = []

for _ in range(n):
    name, dd, mm, yyyy = input().split()
    dd = int(dd)
    mm = int(mm)
    yyyy = int(yyyy)
    arr1.append([yyyy, mm, dd, name])
    arr2.append([yyyy, mm, dd, name])

arr1.sort()
arr2.sort(reverse=True)

print(arr2[0][3]) # 내림차순 정렬
print(arr1[0][3]) # 오름차순 정렬

