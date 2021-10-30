# https://leetcode.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, targer):
            i, j = 0, len(arr)
            while i <= j:
                mid = ( i + j) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            return False
        
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                return binary_search(row, target)
        return False
