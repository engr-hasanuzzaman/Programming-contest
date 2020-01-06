# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# @param {Character[]} letters
# @param {Character} target
# @return {Character}
def next_greatest_letter(letters, target)
  i = last_occure(letters, target)
  if letters[i] == target && i == letters.size - 1
      letters[0]
  elsif letters[i] == target && i == 0
      letters[1]
  else
      letters[(i % letters.size)]
  end
end

def last_occure(letters, target)
  left = 0
  right = letters.size
  
  while left < right
      mid = (left + right) / 2
      
      if letters[mid] == target || target > letters[mid]
          left = mid + 1
      else
          right = mid
      end
  end
  
  left
end