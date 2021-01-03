def count_arrangement(n)
    memo = {}
    memo['count'] = 0 
    arr = (1..n).to_a
    permutation(arr, [], memo)
    memo['count']
  end
  
  def permutation(element, cur_arr, memo)
    if element.size.zero?
      memo['count'] += 1
    end
    
    element.each_with_index do |elm, i|
      if elm % (cur_arr.size + 1) == 0 || (cur_arr.size + 1) % elm == 0
        cur_arr << elm
        permutation(element[0...i] + element[i+1..-1], cur_arr, memo)
        cur_arr.pop()
      end
    end
  end