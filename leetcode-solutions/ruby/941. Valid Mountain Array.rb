# https://leetcode.com/problems/valid-mountain-array/

# @param {Integer[]} a
# @return {Boolean}
def valid_mountain_array(a)
  return false if a.size < 3
  length = a.size
  mi = max_i(a)
  return false if mi.zero? || mi == length -1
  # puts "---mi #{mi}"
  tn = -1
  a[0...mi].each do |n|
      unless n > tn
          return false 
      end
      
      tn = n
  end
  
  tn = a[mi]
  a[mi+1..-1].each do |n|
      unless n < tn
          return false 
      end
      
      tn = n
  end
  
  true
end

def max_i(a)
  max = -1
  mi = 0
  a.each_with_index do |n, i|
      if max < n
          max = n
          mi = i
      end
  end
  
  mi
end