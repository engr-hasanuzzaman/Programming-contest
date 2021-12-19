# https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i, n in enumerate(encoded):
            next_num = arr[i] ^ n
            arr.append(next_num)
        return arr
