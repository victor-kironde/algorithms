def findRotationCount(arr):
  """
  Find the number of rotations of a sorted array
  Number of Rotations = Index of Minimum element (for clockwise rotation)
  The first element (pivot) Properties:
      both prev and next elements are greater than it

  """
  #search space is arr[left..right]
  left = 0
  right = len(arr) - 1
  # iterate until search space contains atleast 1 element
  while (left <= right):

    #if the search space is already sorted, we have found the minimum element (at index left)
    if arr[left] <= arr[right]:
      return left

    mid = int((left + right)/2) # left + (right - left)/2

    #find next and previous elements of the mid element (in circular manner)
    next = (mid + 1) # % len(arr)
    prev = (mid -1) # % len(arr)
    print(prev, next)

    #if mid element is less than both its next and previous neighbor, then it is the minimum element of the array
    if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
      return mid
    #if arr[mid..right] is sorted and mid is not the min element, then pivot element cannot be present in arr[mid..right] and we can discard arr[mid..right] and search in the left half
    elif arr[mid] <= arr[right]:
      right = mid - 1
    # if arr[left..mid] is sorted then pivot element cannot be present in it and we can discard arr[left..mid] and search in the right half
    elif arr[mid] >= arr[left]:
      left = mid + 1
  return -1

# arr = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

arr = [2,3,1]



print("Number of Rotations: " + str(findRotationCount(arr)))