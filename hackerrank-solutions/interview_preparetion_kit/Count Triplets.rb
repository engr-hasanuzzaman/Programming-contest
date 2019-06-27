=begin
  
6 3
1 3 9 9 27 81

output: 6
  
=end

#!/bin/ruby

require 'json'
require 'stringio'

# Complete the countTriplets function below.
def countTriplets(arr, r)
  arr_length = arr.size
  arr_dict = {}
  num_of_consecutive = 0

  arr_length.times do |i|
    cur_num = arr[arr_length - i -1]
    cur_dict_val = arr_dict.dig(cur_num)
    next_dict_val = arr_dict[cur_num * r]

    # update count
    if next_dict_val
      # insert or create dict for current val
      if cur_dict_val
       arr_dict[cur_num] = [cur_dict_val[0] + 1, cur_dict_val[1]]
      else
        arr_dict[cur_num] = [1, next_dict_val[0]]
      end

      num_of_consecutive += (next_dict_val[0] * next_dict_val[1])
    else
      if cur_dict_val
       arr_dict[cur_num] = [cur_dict_val[0] + 1, cur_dict_val[1]]
      else
        arr_dict[cur_num] = [1, 0]
      end
    end
  end

  num_of_consecutive
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

nr = gets.rstrip.split

n = nr[0].to_i

r = nr[1].to_i

arr = gets.rstrip.split.map(&:to_i)

ans = countTriplets arr, r

fptr.write ans
fptr.write "\n"

fptr.close()
