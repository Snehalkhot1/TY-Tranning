arr = [1,0,6,0,70,2,0]
index=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[index]=arr[i]
        index+=1
        while index <len(arr):
            arr[index] = 0
            index+=1
print(arr)