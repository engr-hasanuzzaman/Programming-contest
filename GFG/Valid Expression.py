class Solution:
    def valid(self, s): 
        stack = []
        dict  = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        open_brackets = ["(", "{", "["]
        for i in range(len(s)):
            char = s[i]
            if s[i] in open_brackets:
                stack.append(char)
            else:
                if not stack or stack.pop() != dict[char]:
                    return False
        return len(stack) == 0
