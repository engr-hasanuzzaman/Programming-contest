# https://leetcode.com/problems/edit-distance/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
  row = (0..word2.size).to_a
  for i in 0...word1.size
      temp_row = [i+1]
      for j in 0...word2.size
          if word1[i] == word2[j]
              temp_row[j+1] = row[j]
          else
              temp_row[j+1] = [row[j+1], row[j], temp_row[j]].min + 1
          end
      end 
     
      row = temp_row 
  end
  row.last
end