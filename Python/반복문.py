# 반복문

for number in range(100): # 0 ~ 99
  print(number)

for number in range(95, 100): #95 ~ 99
  print(number)

number = 0
while number < 10 : # 넘버가 10보다 작으면 반복, 10이 되거나 10을 초과하면 끝냄
  print(number)
  number = number + 1


# 조건문

name = "코딩이"

if name == "코딩이" :
  print("니 이름은 코딩이야!")
else :
  print("너의 이름은 코딩이가 아니야!")



#----
# 출력 print()
# 입력 input(), int(input())
# 배열 list(map(str, input().split()))
# 반복문 for _ in range(), while (조건) :
# 조건문 if else