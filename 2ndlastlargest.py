arr =(1,5,8,4,56,9,8,3,4)
l = arr[0]
s = arr[0]
for n in arr:
    if n >l:
        s = l 
        l = n 
    elif n >s and n!= l:
        l = n
print("largest element :",l)