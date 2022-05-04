# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        char_count = 0
        for idx, char in enumerate(chars):
            char_count += 1
            if idx < len(chars) - 1 and chars[idx+1] == char:
                continue

            # update left most cell with current char: a b b b b c c c -> a b 2 c 3
            chars[left] = char
            if char_count > 1:
                count_size = len(str(char_count))
                for i in range(count_size, 0, -1):
                    chars[left+i] = str(char_count % 10)
                    char_count //= 10
                left += count_size + 1
            else:
                left += 1

            # reset counter
            char_count = 0
        return left
