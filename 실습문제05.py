
num = [3,10,20]
total = 0
for n in num :
   total += n
print(total/3)



## 멘토님 풀이
nums = [3, 10, 20] #문제제공

result = 0
count =0    #값 초기화

for num in nums : # 반복문
   result = result + num
   count = count + 1
print(result/ count)