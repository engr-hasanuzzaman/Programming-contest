# https://leetcode.com/problems/palindrome-permutation-ii/

from collections import Counter

# intution: number of odd char in palindrom string is at most one
# if we generate char freq and take char with freq > 1 then permuation of these char list will be the half of the palindrom
# we can rev the string to get the other half of the palindrom


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        char_frequency = Counter(s)
        half_palindrom_chars = []
        odd_counter = 0
        odd_char = None

        for char, freq in char_frequency.items():
            if freq % 2 == 1:
                odd_counter += 1
                odd_char = char

            # hanlde both, a -> 2, b -> 3 :abbba, babab
            for i in range(freq//2):
                half_palindrom_chars.append(char)

            # not palindrom
            if odd_counter > 1:
                return []

        generated = defaultdict(bool)
        ans = []
        for per in permutations(half_palindrom_chars):
            per_string = "".join(per)
            if generated[per_string]:
                continue
            generated[per_string] = True
            if odd_char:
                ans.append(f"{per_string}{odd_char}{per_string[::-1]}")
            else:
                ans.append(f"{per_string}{per_string[::-1]}")
        return ans
