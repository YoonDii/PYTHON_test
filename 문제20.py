#정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.

n = input() #123
a = 0
for n in str(n): #문자열로 변환 후 다시 정수로 변환
    a += int(n) 
print(a)  #6



#멘토님 풀이
n = 123
# n이 0일때 stop!
result = 0
while n :
    # 몫은 다음 n이 됨.
    # 나머지는 더해나가면 된다!
    result += n % 10
    n //= 10
print(result)

#멘토님 풀이2
# divmod(x, y)는 x를 y로 나누고, 결과를tuple로 변환
n = 123
result = 0
while n :
    n, remainder = divmod(n , 10)
    result += remainder
print(result)
