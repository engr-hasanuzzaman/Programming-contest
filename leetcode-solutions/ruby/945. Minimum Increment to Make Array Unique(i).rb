# @param {Integer[]} a
# @return {Integer}
def min_increment_for_unique(a)
  move = 0
  tar_num = 0
  
  a.sort.each do |n|
      move += [tar_num - n, 0].max
      tar_num = [n + 1, tar_num + 1].max
  end
  
  move
end