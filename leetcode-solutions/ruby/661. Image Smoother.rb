# https://leetcode.com/problems/image-smoother/

# @param {Integer[][]} m
# @return {Integer[][]}
def image_smoother(m)
  m_size = m.size
  m_size.times do |i|
      r_size = m[i].size
      r_size.times do |j|
          sum = 0
          counter = 0
          
          # number
          if m[i][j]
              counter += 1
              sum += m[i][j]
          end
          
          #top left corner
          if m[i-1] && m[i-1][j-1]
              counter += 1
              sum += m[i-1][j-1]
          end
          
          #top item
          if m[i-1] && m[i-1][j]
              counter += 1
              sum += m[i-1][j]
          end
          
          # top right corner
          if m[i-1] && m[i-1][j+1]
              counter += 1
              sum += m[i-1][j+1]
          end
          
          # rigth
          if m[i][j+1]
              counter += 1
              sum += m[i][j+1]
          end
          
          # right below corner
          if m[i+1] && m[i+1][j+1]
              counter += 1
              sum += m[i+1][j+1]
          end
          
          # below     
          if m[i+1] && m[i+1][j]
              counter += 1
              sum += m[i+1][j]
          end
          
          # below left corner
          if m[i+1] && m[i+1][j-1]
              counter += 1
              sum += m[i+1][j-1]
          end
          
          # left
          if m[i][j-1]
              counter += 1
              sum += m[i][j-1]
          end
          
          puts "sum #{sum} c#{counter} #{i} #{j}"
          m[i][j] = (sum/counter).floor
      end
  end
    m
end

p image_smoother([[1,1,1,2,3,4],
  [1,1,1,0,2,3],
  [1,1,1,0,0,0]])