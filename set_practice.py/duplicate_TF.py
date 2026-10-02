# arr = list(map(int,input("Enter the Elements :").split()))
# seen = set()
# for x in arr:
#     if x in seen:
#         print(True)
#         break
#     seen.add(x)
# else:
#     print(False)


arr = list(map(int,input("Enter the Elements :").split()))
if len(arr) != len(set(arr)):
    print(True)
else:
    print(False)