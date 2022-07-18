word = "HappyHacking"

count = 0
x = "a","e","i","o","u"
for char in word:
    if char in x:
        count += 1

print(count)