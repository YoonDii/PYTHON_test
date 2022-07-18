n = [0,20,100]

minnum = n[0]
for a in range(1, len(n)) :
    if minnum > n[a] :
        minnum = n[a]
print(minnum)