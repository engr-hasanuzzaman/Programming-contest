# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [int(i) for i in a[::-1]]
        b = [int(i) for i in b[::-1]]
        i = j = rem = 0
        ans = []
        while i < len(a) and j < len(b):
            digit = a[i] ^ b[j] ^ rem
            ans.append(digit)
            rem = (a[i] & b[j]) or (a[i] & rem) or (b[j] & rem)
            i += 1
            j += 1

        if i != len(a):
            while i < len(a):
                digit = a[i] ^ rem
                rem = a[i] & rem
                ans.append(digit)
                i += 1
        
        if j != len(b):
            while j < len(b):
                digit = b[j] ^ rem
                rem = b[j] & rem
                ans.append(digit)
                j += 1

        if rem == 1:
            ans.append(rem)
        return "".join([str(n) for n in ans[::-1]])
