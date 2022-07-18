word = input()
dict = {}

for i in word:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for k,v in dict.items():
    print(k, v)


## 멘토님 풀이

word = input()

result = {}
for char in word:
    if not char in result: #딕셔너리에 키가 없으면?
        result[char] = 1 # 키랑 값을 1로 초기화한다.
    else:
        result[char] = result[char] + 1
print(result)


result = {}
for char in word:
    result[char] = result.get(char, 0) + 1
print(result)
#출력부분
for key in result:
    print(key, result[key])
