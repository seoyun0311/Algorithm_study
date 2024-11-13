import sys
input = sys.stdin.readline

N = int(input())
arr1 = sorted(list(map(int, input().split())))

M = int(input())
arr2 = list(map(int, input().split()))

for number in arr2:
  s = 0
  e = N - 1
  flag = False

  while s <= e: # 만약 교차 되지 않는다면
      mid = (s+e)//2

      if arr1[mid] == number: # 정답
        flag = True
        break

      elif arr1[mid] > number: # 다운
        e = mid - 1

      elif arr1[mid] < number: # 업
        s = mid + 1

  if flag : print(1)
  else : print(0)

