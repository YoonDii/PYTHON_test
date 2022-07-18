word = 'apple'

x ='a', 'e', 'i', 'o', 'u'
count = 0

for char in word:
    if char in x:
        count += 1
print(count)


word = 'aeiou'

x ='a', 'e', 'i', 'o', 'u'
count = 0

for char in word:
    if char in x:
        count += 1
print(count)


word = 'zxcvb'

x ='a', 'e', 'i', 'o', 'u'
count = 0

for char in word:
    if char in x:
        count += 1
print(count)


## 멘토님 풀이
word = input()
count = 0
for char in word :
    if char in 'aeiou':
        count += 1
print(count)