arr=[1,2,3,4,5,6]
temp = arr[4]
for i in range(4,0,-1):
    arr[i] = arr[i-1]
arr[0] = temp
print(arr[:5])