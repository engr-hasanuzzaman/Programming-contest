# @param {Integer} n
# @return {String[]}
def fizz_buzz(n)
    result = []
    
    1.upto(n) do |number|
      
     result <<  case
                when number % 3 == 0 && number % 5 == 0 then 'FizzBuzz'    
                when number % 3 == 0 then 'Fizz'
                when number % 5 == 0 then 'Buzz'
                else "#{number}" 
                end
    end
    
    result
end
