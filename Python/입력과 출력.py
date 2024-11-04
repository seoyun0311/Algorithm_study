# 입력을 받고( 디테일! )

# Default input 스트링 타입, 문자열 타입으로 받아와주도록 만들어짐!


# 배열! 공간에다가 숫자나 문자를 담을 수 있음
list = [0,0,0,0]
list = ["he", "hi", "hu"]

# Case 1 : 단순히 정수 일때,
number =  int(input())

# Case 2 : 수열
list1 = list(map(int, input().split()))

print(list1)

# Case 3 : 단순히 문자 일때,
string = input()

# Case 4 : 문자열
list2  = list(map(str, input().split()))
print(list2)
print(*list2)

# 계산을 하고


# 출력을 한다
print(number + number) # 24
print(string + string) # 1212

# ------ 입문자 준비 강의 ----- 
# 숫자를 입력 받을 때는 int(input())
# 문자를 입력 받을 때는 input()

# 여러가지 숫자들의 조합, 수열
list(map(int, input().split))
# 여러가지 문자들의 조합, 문자열
list(map(str, input().split))