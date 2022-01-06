# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        self.combination(0, mapping, ans, "", digits)
        return ans
        
    def combination(self, index, mapping, ans, cur_com, digits):
        if index == len(digits):
            ans.append(cur_com)
            return
        for _, c in enumerate(mapping[digits[index]]):
            self.combination(index + 1, mapping, ans, cur_com + c, digits)
