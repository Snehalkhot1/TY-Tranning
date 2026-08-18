arr = [2, 7, 11, 15]
target = 9

def two_sum(arr, target):
    seen = set()

    for num in arr:
        needed = target - num

        if needed in seen:
            return [arr.index(needed), arr.index(num)]

        seen.add(num)

    return []

print(two_sum(arr, target))