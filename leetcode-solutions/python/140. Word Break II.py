# https://leetcode.com/problems/word-break-ii/

from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = defaultdict()
        memo[''] = []
        return self.get_sentences(s, wordDict, memo)

    def get_sentences(self, text, wordDict, memo):
        if text in memo:
            return memo[text]

        sentences = []
        for idx in range(len(text)):
            sub_str = text[0:idx+1]

            if sub_str in wordDict:
                # handle last part of the sentence
                if idx == len(text) - 1:
                    sentences.append(sub_str)
                    continue

                partial_sentences = self.get_sentences(
                    text[idx+1:], wordDict, memo)
                temp_sentences = [sub_str + " " + s for s in partial_sentences]
                sentences += temp_sentences

        memo[text] = sentences
        return sentences
