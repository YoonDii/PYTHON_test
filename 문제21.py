# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지


n = input('') #1234
n_list = list(n)
n_list.reverse()

print(''.join(n_list)) #4321


#가장 간단한 풀이는 str쓰는것.
#pritn(int(str(n)[::-1]))

#멘토님풀이
n = 1234
result = 0
while n :
    # 이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += n%10
    # n을 깎는다.
    n //= 10
print(result)
