# 입력 : 키 순서대로 번호 부여
# 키가 가장 작은 아이가 1번
# 강산이네 반 아이들은 20명
# 같은 키를 가진 학생은 없음
# 1. 아무나 한 명을 뽑아 줄의 맨 앞에 세움
# 2. 한 명씩 줄의 맨 뒤에 서면서 다음과 과정을 거친다.
# 3. 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 4. 자기 앞에 자기보다 키 큰 학생이 한 명 이상 있다면 그 중 가장 앞에 있는 학생의 바로 앞에 선다.
# 5. a부터 그 뒤의 모든 학생들은 한 칸씩 뒤로 간다.
# 출력 : 학생들이 총 몇번 뒤로 물러서게 되는지

P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(1, len(arr)-1):
       for j in range(i+1, len(arr)):
           if arr[i] > arr[j]:
               arr[i], arr[j] = arr[j], arr[i]
               answer += 1
    print(arr[0], answer)
