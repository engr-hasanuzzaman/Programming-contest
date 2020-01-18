# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

# @param {String[]} list1
# @param {String[]} list2
# @return {String[]}
def find_restaurant(list1, list2)
  ans = []
  i_sum = list1.size + list2.size
  m1 = {}
  m2 = {}
  m_size = list1.size > list2.size ? list1.size : list2.size
  
  m_size.times do |i|
      if list1[i] && list2[i]
          m1[list1[i]] = i
          m2[list2[i]] = i
      elsif list1[i]
          m1[list1[i]] = i
      else
          m2[list2[i]] = i
      end
      
      # handle duplicate
      if list1[i] == list2[i]
          sum = m1[list2[i]] + i

          if  sum < i_sum
              ans = []
              ans << list2[i]
              i_sum = sum
          elsif sum == i_sum
              ans << list2[i]
          end
      else
          # check map 1 with list2 data
          if m1[list2[i]]
              sum = m1[list2[i]] + i

              if  sum < i_sum
                  ans = []
                  ans << list2[i]
                  i_sum = sum
              elsif sum == i_sum
                  ans << list2[i]
              end
          end
          
          # check map 2 with list1 data
          if m2[list1[i]]
              sum = m2[list1[i]] + i

              if  sum < i_sum
                  ans = []
                  ans << list1[i]
                  i_sum = sum
              elsif sum == i_sum
                  ans << list1[i]
              end
          end
      end
          
  end
  
  ans
end