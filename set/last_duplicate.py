def check(arr):
    unique = set()

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in unique:
            return arr[i]
        unique.add(arr[i])

    return -1


arr = [1, 2, 2, 3, 4, 4, 5]

print(check(arr))