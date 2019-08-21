# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
#!/bin/ruby

require 'json'
require 'stringio'

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year)
    if year == 1918
        "26.09.1918"
    elsif year < 1918
        if year % 4 == 0
            "12.09.#{year}"
        else
            "13.09.#{year}"
        end
    else
        if (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)
            "12.09.#{year}"
        else
            "13.09.#{year}"
        end 
    end
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

year = gets.strip.to_i

result = dayOfProgrammer year

fptr.write result
fptr.write "\n"

fptr.close()
