word = input()
for i in range(len(word)):
  if word[i] == 'a':
    break
  if i == len(word)-1:
    i = -1
    break
print(i)

# 추가문제
word = input()

for i in range(len(word)):
  if word[i] == 'a':
    print(i,end=' ')



##멘토님 풀이
word = input()

for idx in range(len(word)):
  if word[idx] == 'a':
      print(idx)
      break
else:
    print(-1)