# Construct and update binary index tree

# Ruby implementation of Binary Indexed Tree 

# Returns sum of arr[0..index]. This function assumes 
# that the array is preprocessed and partial sums of 
# array elements are stored in BITree[]. 
def sum(tree, i)
  current = 1 # our bit is 1 based
  sum = 0

  while current <= i + 1
    sum += tree[current]
    current += (current & -current) 
  end

  sum
end

# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def update_bit(tree, i, val)
  current = i + 1
  while current <= tree.size
    tree[current] += val
    current += (current & -current)
  end  
end

# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr)
  bst = Array.new(arr.size+1){0}
  arr.each_index do |i|
    update_bit(bst, i, arr[i])
  end

  bst
end

# Driver code to test above methods 
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
BITTree = construct(freq) 
puts "BITree is #{BITTree}"
puts("Sum of elements in arr[0..5] is #{sum(BITTree,5)}")
# freq[3] += 6
update_bit(BITTree, 3, 6) 
puts("Sum of elements in arr[0..5] after update is #{sum(BITTree, 5)}") 

# This code is contributed by Raju Varshney 
