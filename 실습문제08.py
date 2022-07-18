nums = [0, 20, 100]
nums = set(nums)
nums = list(nums)
nums.sort()

print(nums[-2])


## 멘토님 풀이

numbers = [0, 20, 100, 40] ##문제제공
max_number = numbers[0]   #초기값 설정
s_number = numbers[0]

for n in numbers:  # 전체반복문 설정
    if max_number < n:
        s_number = max_number
        max_number = n
    elif s_number < n < max_number :
         s_number = n
         s_number < n and n < max_number
print(s_number)