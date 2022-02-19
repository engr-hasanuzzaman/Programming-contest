class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        word_list = S.split(".")
        start, end = 0, len(word_list) - 1
        
        while start < end:
            word_list[start], word_list[end] =  word_list[end], word_list[start]
            start += 1
            end -= 1
        return ".".join(word_list)
