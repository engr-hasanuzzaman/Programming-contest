def ThreeSum(arr)
  return false if arr.size < 4
  
  sum = arr.shift()

# arr.sort!
  num_dict = Hash.new(0)
  arr.each{|c| num_dict[c] += 1 }

  (0..arr.length - 3).each do |i|
    (i+1..arr.length - 1).each do |j|
      t_n = sum - arr[i] - arr[j]
      # is target number exist
      # puts "#{t_n} #{arr[i]} #{arr[j]}"
      if num_dict[t_n] > 0
        # puts "----tn exist #{t_n} #{arr[i]} #{arr[j]}"
        # check same number issue
        if t_n == arr[i] || t_n == arr[j]
          # puts "duplicate"
          if arr[i] == arr[j]
            return true if num_dict[t_n] == 3
          else
            return true if num_dict[t_n] == 2
          end
        else
          return true  
        end
        # check duplicate
        
      end # check dic

    end
  end
  # No matches found
  false
end
 
puts ThreeSum( [10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 5, 5, 5, 8, -2, -2, -2, -2, -1, 7])