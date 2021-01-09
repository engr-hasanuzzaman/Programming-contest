# https://leetcode.com/problems/word-ladder/
# Use BFS to find next next formable word and track remaining word list
# and for each word list always search on remaining word list (those are not picked in the queue yet)
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        step = 1
        rem_word_list = []
        while q:
          c_size = len(q)
          step += 1
          # pick each element and find there transformable words
          for _ in range(c_size):
            current = q.pop()
            rem_word_list = []
            for w in wordList:
              if Solution.transformable(w, current):
                if w == endWord:
                  return step
                q.appendleft(w)
              else:
                rem_word_list.append(w)
            # at the end of eac search update remaining work otherwise rem_word_list will have
            # duplicate word
            wordList = rem_word_list
        return 0
        
    # chec where one strign to other is transformable by changing one character
    def transformable(str1, str2):
      max_diff = 1
      for i in range(len(str1)):
        if str1[i] != str2[i]:
          max_diff -= 1
        if max_diff < 0:
          break
      return max_diff >= 0
    
b = "ymain"
e = "oecij"
words = ["ymann","yycrj","oecij","ymcnj","yzcrj","yycij","xecij","yecij","ymanj","yzcnj","ymain"]
s = Solution()
print(s.ladderLength(b, e, words))