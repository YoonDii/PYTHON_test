word = input()

result = ''
for x in word:
    aph = ord(x)
    aph -= 32
    result += chr(aph)

print(result)



#멘토님 풀이
