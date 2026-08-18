arr= [1,2,3,3,4,5]
dup = []
original = []
for i in arr:
    if i not in original:
        original.append(i)
    else:
        dup.append(i)
print(dup)
print(original)