def findRotationCount(arr):
  start = 0
  end = len(arr) - 1
  while (start <= end):
    if arr[start] <= arr[end]:
      return start
    mid = int((start + end)/2)
    next = (mid + 1)
    prev = (mid -1)


    if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
      return mid
    #find the sorted side in order to drop it.
    elif arr[mid] <= arr[end]:
      end = mid - 1
    else:
      start = mid + 1
  return -1

# arr = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

arr = [2,3,1]



print("Number of Rotations: " + str(findRotationCount(arr)))