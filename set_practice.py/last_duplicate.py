arr = list(map(int,input("Enter the Element :").split()))
seen = set()
last_duplicate = None
for x in arr:
    if x in seen :
        last_duplicate = x
    else:
        seen.add(x)
print("last duplicate element is :", last_duplicate)