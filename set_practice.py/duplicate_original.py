arr = list(map(int,input("Enter the elements :").split()))
original= set()
duplicate = set()
for x in arr:
    if x in original:
        duplicate.add(x)
    else:
        original.add(x)
print(original)
print(duplicate)