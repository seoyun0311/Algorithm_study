# 완전탐색
# 정수론(공약수)

# 17과 42의 공약수 GCD 계산 ! 1이라면 pass 아니라면 non pass

# gcd(42, 2184) != 1

# 두수를 비교해서 최대공약수가 1이라면 OK

# 두 수를 비교해서 최대공약수가 1이라면 NON OK

# 숫자를 하나 추가하거나 
# 또는 두 개 추가한다. 

for i in range(42, 2184):
  if gcd(42, i) == 1:
    if gcd(2184, i) == 1:
        count += 1
        break
    
for j in range(2184, 2200):
   if gcd(42, i) == 1:
      if gcd(2184, i) == 1:
         count += 1
         break
   if j == 2199