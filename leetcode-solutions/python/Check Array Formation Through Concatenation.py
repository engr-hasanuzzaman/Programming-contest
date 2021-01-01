# Check Array Formation Through Concatenation
```
You are given an array of distinct integers arr and an array of integer arrays pieces, 
where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays 
in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
Return true if it is possible to form the array arr from pieces. Otherwise, return false.
```
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        c_array = []
        i = 0
        while i < len(arr):
            found = False
            for j in range(len(pieces)):
                if pieces[j][0] == arr[i]:
                    found = True
                    c_array += pieces[j] 
                    i += len(pieces[j])
                    del pieces[j]
                    break
            if not found:
                return False
        # check equal number of element
        if len(arr) != len(c_array) or len(pieces) != 0:
            return False
    
        for i in range(len(arr)):
            if arr[i] != c_array[i]:
                return False
        
        return True
       