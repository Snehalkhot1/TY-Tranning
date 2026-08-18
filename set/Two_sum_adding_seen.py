arr = [2, 7, 11, 15]
target = 9

seen = set()

for num in arr:
    needed = target - num

    if needed in seen:
        print("Pair found")
        break

    seen.add(num)

print("Elements in seen:", seen)
print("Sum of seen:", sum(seen))