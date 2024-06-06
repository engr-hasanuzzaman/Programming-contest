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


