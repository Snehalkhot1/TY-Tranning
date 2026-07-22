arr = [1, 2, 3, 2, 4, 5, 1, 6, 3]
num = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in num:
            print(arr[i])
            num.append(arr[i])