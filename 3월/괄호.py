# 괄호는 ( )
# 괄호의 모양이 바르게 구성된 문자열 VPS = ()
# x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열 (x)도 VPS
# 두 VPS x와 y를 접합 시킨 새로운 문자열 xy도 VPS
# (())() 는 vps지만 (() 모두 vps가 아닌 문자열

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    count = 0
    is_vps = True

    for ch in s:
        if ch == '(':
            count += 1
        else: # ch == ')'
            count -= 1

        if count < 0:
            is_vps = False
            break
        
    if is_vps and count == 0:
        print("YES")
    else:
        print("NO")

# 짝수 길이인지 확인
# 여는 괄호면 +1
# 닫는 괄호면 -1
# 중간에 count < 0 이면 바로 NO
# 끝났을 때 count == 0 이면 YES