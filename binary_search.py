def binary_search(arr, n, el):
  start = 0
  end = n-1
  while start <= end:
    mid = int((start + end)/2)
    if el == arr[mid]:
      return mid
    elif el > arr[mid]:
      start = mid + 1
    else:
      end = mid-1
  return -1

arr = [3,4,5,1,2]
print(binary_search(arr, 6, 1))



