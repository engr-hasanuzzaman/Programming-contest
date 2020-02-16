# https://www.hackerrank.com/challenges/count-triplets-1/problem

def countTriplets(arr, r)  
  r_count = Hash.new {0}
  l_count = Hash.new {0}
  
  arr.each do |n|
    if r_count[n]
        r_count[n] += 1
    else 
        r_count[n] = 1
    end 
  end

  ans = 0  
  arr.each do |i|
    r_count[i] -= 1

    if i % r == 0
      ans += l_count[i/r] * r_count[i*r]
    end
    
    if l_count[i]
        l_count[i] += 1  
    else 
        l_count[i] = 1  
    end    
  end

  ans 
end