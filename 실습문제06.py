n = [0,20,100]

maxnum = n[0]
for a in range(1, len(n)) :
    if maxnum < n[a] :
        maxnum = n[a]
print(maxnum)


## 멘토님 풀이

nums = [0, 20, 100, 40 ]
max_num = float("-inf")
for n in nums:
    if  max_num < n :
        max_num = n
    print(max_num)