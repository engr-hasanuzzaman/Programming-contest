class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        size = len(shifts)
        ans = [None] * len(s)
        # print(ans)
        array_sum = 0
        
        for i in range(len(shifts) - 1, -1, -1):
            ordVal = ord(s[i])
            array_sum += shifts[i]
            shift = array_sum % 26
            newOrd = ordVal + shift
            
            if newOrd > 122:
                newOrd = (newOrd % 123) + ord('a')
                ans[i] = chr(newOrd)
            else:
                ans[i] = chr(newOrd)
            
        
        return "".join(ans)
        
        
        