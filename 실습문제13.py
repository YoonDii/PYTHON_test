str = 'apple'

new_str = str[::-1]
print(new_str)


## 멘토님 풀이

word = 'apple'
result = ''
for char in word:
    result = char + result
print(result)