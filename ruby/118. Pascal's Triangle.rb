# @param {Integer} num_rows
# @return {Integer[][]}
def generate(num_rows)
    # declare 2d arrat with size other wise we will get
    # call [] on nil class
    result = Array.new(num_rows) { Array.new(num_rows) }
    
    num_rows.times do |row|
        row.succ.times do |element|
            result[row][element] = generate_pascal_number(row, element)
        end
        
        # remove unwanted nil value from array
        result[row] = result[row].compact
    end
    
    return result
end

# both are zero baseed
# if row is n ane element is r then pascal numbe is
# n! / r! (n-r)!
def generate_pascal_number(row, element)
  row.fact / ((row - element).fact * element.fact)
end

# There is no standard factorial function in ruby
# Redeclare Integer class and define fact method
# default inject 1 for 0!
class Integer
    def fact
        (1..self).reduce(1, :*)
    end
end
