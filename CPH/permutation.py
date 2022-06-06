def permutation(arr, start = 0, ans = [] ):
  if start >= len(arr):
      ans.append(arr[:])
      return

  for i in range(start, len(arr)):
    arr[i], arr[start] = arr[start], arr[i]
    permutation(arr, start+1, ans)
    arr[i], arr[start] = arr[start], arr[i]
  return ans
print(permutation([1,2,3]))