# https://leetcode.com/problems/perfect-squares/

# @param {Integer} n
# @return {Integer}
def num_squares(n)
  m_perfecta_sqr(n)
end

def m_perfecta_sqr(n)
   return n if n <= 3
   
   # b is perfect sqr
   return 1 if Math.sqrt(n).to_i * Math.sqrt(n).to_i == n
   
   # reuse ans
   dp = [0,1,2,3]
   # dp[n] = n # max num of psqr could be n
   
   4.upto(n) do |i|
       dp[i] = i
       
       1.upto(Math.sqrt(i).ceil) do |j|
           temp = j * j
           break if temp > i
           # puts "j #{j}, #{dp}"
           dp[i] = [dp[i], 1+dp[i-temp]].min
       end
   end
   
   dp[n]
end
