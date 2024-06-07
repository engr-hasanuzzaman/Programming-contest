# https://www.geeksforgeeks.org/problems/most-frequent-word-in-an-array-of-strings3528/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article


# User function Template for python3
from collections import Counter, defaultdict

class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        # code here
        frequency_map = Counter(arr)
        word_with_max_freq = ""
        cur_size = 0
        last_idx = n -1
        has_seen = defaultdict(lambda: False)
        # print(frequency_map)
        for word in arr:
            # word = arr[idx]
            if frequency_map.get(word) > cur_size or (frequency_map.get(word) == cur_size and not has_seen.get(word)):
                cur_size = frequency_map.get(word)
                word_with_max_freq = word
                has_seen[word] = True
                
                
        return word_with_max_freq


# using trie dataStructure
from collections import defaultdict
class Solution:
    
    #Function to find most frequent word in an array of strings.
    def mostFrequentWord(self,arr,n):
        freq_word = ""
        cur_max_freq = 0
        cur_start_index = 0
        trie = TrieNode()
        
        
        for idx in range(n):
            word = arr[idx]
            cur_node = trie
    
            for char in word:
                if cur_node.childrens[char] is None:
                    cur_node.childrens[char] = TrieNode()
                cur_node = cur_node.childrens[char]
            cur_node.word_count += 1
            if cur_node.word_count == 1:
                cur_node.first_index = idx
        
    
            if cur_node.word_count > cur_max_freq or (cur_node.word_count == cur_max_freq and cur_node.first_index > cur_start_index):
                freq_word = word
                cur_max_freq = cur_node.word_count
                cur_start_index = cur_node.first_index
        return freq_word
    

class TrieNode:
  def __init__(self):
      self.childrens = defaultdict(lambda: None)
      self.word_count = 0
      self.first_index = 0
      

