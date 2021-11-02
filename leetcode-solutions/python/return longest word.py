import re

def LongestWord(sen):
  max_size = 0
  words = sen.split(" ")
  for word in words:
    out = re.sub(r'[^a-zA-Z0-9\s]', '', word)
    max_size = max(max_size, len(out))
  
  for word in words:
    out = re.sub(r'[^a-zA-Z0-9\s]', '', word)
    if len(out) == max_size:
      return word
  
# keep this function call here 
print(LongestWord(input()))