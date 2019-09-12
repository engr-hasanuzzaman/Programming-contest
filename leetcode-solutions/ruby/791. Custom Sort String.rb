  # https://leetcode.com/problems/custom-sort-string/

  # @param {String} s
  # @param {String} t
  # @return {String}
def custom_sort_string(s, t)
  t_dict = Hash.new(0)
  ans = []
  t.each_char do |c|
      t_dict[c] += 1
  end
  
  s.each_char do |c|
      if t_dict[c] > 0
          t_dict[c].times{ans << c}
          t_dict.delete(c)
      end
  end
  
  t_dict.each do |k,v|
      v.times{ans<<k}
  end
  
  ans.join
end