# longest prefix which is suffiex also
# pi[i] contains length of the max sub-string with end at i and which is prefix also
# so pi[i] will contatin the next char with is not part of the prefix yet
# [use lps for pattern matching](https://files.codingninjas.in/article_images/prefix-function-knuth-morris-pratt-algorithm-1-1635309294.jpg)
def lps(str):
    pi = [0] * len(str)

    for i in range(1, len(str)):
        # j is the prfix size, that means jth element is next after matching string
        j = pi[i-1]
        while j > 0 and str[j] != str[i]:
            j = pi[j-1]

        # if we find any match, then increase the size by one
        if str[j] == str[i]:
            j += 1
        pi[i] = j
    return pi

def kmp(str, pat):
    prefix_array = lps(pat)
    i = j = 0
    while i < len(str):
        # if it is matching then increment i
        if str[i] == pat[j]:
            if j == len(pat) - 1:
                print("string matching found", i-len(pat)+1)
                return 
            j += 1
        else:
            if j > 0:
                j = prefix_array[j-1]
                continue
        # if j = 0, that menas there is not option of matching ith value, increment i to next char
        i += 1
    return False
        
       
            
print(kmp("ABABDABACDABABCABAB", 'ABABCABAB'))