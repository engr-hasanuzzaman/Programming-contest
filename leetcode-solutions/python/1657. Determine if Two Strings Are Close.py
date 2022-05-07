from collections import defaultdict, Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        return self.is_anagram(word1, word2) or (self.has_same_char(word1, word2) and self.is_same_char_freq(word1, word2))

    def is_anagram(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        frequency = defaultdict(int)
        for i in range(len(word1)):
            frequency[word1[i]] += 1
            frequency[word2[i]] -= 1

        for num in frequency.values():
            if num != 0:
                return False

        return True

    def is_same_char_freq(self, word1: str, word2: str) -> bool:
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

    def has_same_char(self, word1: str, word2: str) -> bool:
        present = defaultdict(bool)

        for i in range(len(word1)):
            present[word1[i]] = True

        for i in range(len(word1)):
            if not present[word2[i]]:
                return False

        return True

# sorter solution
# if both string have same chars (if s1 has a then b need to has a tool) and char frequency counter is same, 
# aab ->bba (2, 1) then according to the rules they are transformable
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
