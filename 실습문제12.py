str = 'apple'

new_str = str.replace('a', '')
print(new_str)



## 멘토님 풀이

word = 'apple'
result = ''
for char in 'apple':
    if char != 'a':
        result = result + char
print(result)
    