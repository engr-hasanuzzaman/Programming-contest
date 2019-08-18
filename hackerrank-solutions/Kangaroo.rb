#!/bin/ruby

require 'json'
require 'stringio'

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2)
  return 'YES' if x1 == x2
  
  if x1 < x2
    return 'NO' if v1 <= v2

    while x1 < x2
      x1 += v1
      x2 += v2
      return 'YES' if x1 == x2
    end

  else
    return 'NO' if v2 <= v1

    while x2 < x1 do
      x1 += v1
      x2 += v2
      return 'YES' if x1 == x2
    end
  end  

  'NO'    
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

x1V1X2V2 = gets.rstrip.split

x1 = x1V1X2V2[0].to_i

v1 = x1V1X2V2[1].to_i

x2 = x1V1X2V2[2].to_i

v2 = x1V1X2V2[3].to_i

result = kangaroo x1, v1, x2, v2

fptr.write result
fptr.write "\n"

fptr.close()
