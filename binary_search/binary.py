import bisect 

arr = sorted(list(range(0, 20, 2))*3)
print(arr)
# returns the index where the element should be inserted if already exists then returns current first index
# same as lower bound
print(bisect.bisect_left(arr, 2))
print(bisect.bisect_left(arr, 3))

print()
# returns the index where the element should be inserted if already exists then returns current last index
# same as upper bound
print(bisect.bisect_right(arr, 2))
print(bisect.bisect_right(arr, 3))


print()
# similar to bisect_right
# same as upper bound
print(bisect.bisect(arr, 2))
print(bisect.bisect(arr, 3))