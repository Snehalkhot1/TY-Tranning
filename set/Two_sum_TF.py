arr = [2, 7, 11, 15]
target = 9

def check(arr, target):
    seen = set()

    for num in arr:
        needed = target - num

        if needed in seen:
            return True

        seen.add(num)

    return False

print(check(arr, target))