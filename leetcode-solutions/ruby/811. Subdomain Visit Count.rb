# https://leetcode.com/problems/subdomain-visit-count/

# @param {String[]} cpdomains
# @return {String[]}
def subdomain_visits(cpdomains)
  count_hash = Hash.new(0)
  
  cpdomains.each do |d|
      count, domain = d.split
      
      count_hash[domain] += count.to_i
      s_domains = domain.split(".")
      1.upto(s_domains.size - 1) do |i|
          count_hash[s_domains[i..-1].join(".")] += count.to_i
      end
      
  end
  
  result = []
  count_hash.each do |k, v|
      result << "#{v} #{k}"
  end
  
  result
end