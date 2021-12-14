# https://leetcode.com/problems/license-key-formatting/

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
            s = "".join(s.upper().split("-"))
            size = len(s)
            res = []
            i = size_of_first_word = size % k
            if size_of_first_word > 0:
                res.append(s[:size_of_first_word])

            while i < size:
                res.append(s[i:i + k])
                i += k
            return "-".join(res)
