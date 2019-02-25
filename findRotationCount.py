def findRotationCount(arr):
  left = 0
  right = len(arr) - 1
  while (left <= right):
    if arr[left] <= arr[right]:
      return left
    mid = int((left + right)/2)
    next = (mid + 1)
    prev = (mid -1)
    print(prev, next)

    if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
      return mid
    elif arr[mid] <= arr[right]:
      right = mid - 1
    elif arr[mid] >= arr[left]:
      left = mid + 1
  return -1

# arr = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

arr = [2,3,1]



print("Number of Rotations: " + str(findRotationCount(arr)))