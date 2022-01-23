### heap is a complete binary tree in which each node has <= or >= value compare of all it's decendent. If root keep min, it is min heap, if root contatin max then it is max heap
- when adding a new element on the heap, first it has to be added on the leaf then adjust the nodes (swap with the parent untill it the value is greater than it's parent)
- we only can delete elment from the heap root (not from any other places)
## steps for delete
- delete the root
- pick the last element as the root and adjust the heap property
    - replce with max child repetedly untill new value become correct root
**N.B: for insertion, adjustment is done from leaf to parent but for delete operation adjustment happens from root to leaf 

## Heap sort has two step
- make heap using input elements
- delete element one by one and put at the end of the heap array which is a sorted array