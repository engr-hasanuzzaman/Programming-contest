# https://leetcode.com/problems/find-the-town-judge/

# @param {Integer} n
# @param {Integer[][]} trust
# @return {Integer}
def find_judge(n, trust)
  return -1 if trust.size.zero?
  return trust.first.last if trust.size == 1
  
  trust_dict = {}
  trust.each do |a|
      # puts "---a #{a}"
      if trust_dict[a.first]
          trust_dict[a.first] << a.last
      else
          trust_dict[a.first] = [a.last]
      end
  end
  
  # puts "---#{trust_dict}"
  town_judge = trust_dict.values.first
  # puts "---#{town_judge}"
  trust_dict.values.each do |a|
      town_judge = a 
  end
  
  # puts "---#{town_judge}"
  town_judge.first || -1
end