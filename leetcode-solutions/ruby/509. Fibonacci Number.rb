# https://leetcode.com/problems/fibonacci-number/

# @param {Integer} n
# @return {Integer}
@cache = {}
def fib(n)
  return n if n < 2
  return @cache[n] if @cache[n]
    
  result = fib(n-1) + fib(n-2)
  @cache[n] = result   
  result  
end
