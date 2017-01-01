# @param {Integer} row_index
# @return {Integer[]}
def get_row(row_index)
    result = []
    
    row_index.succ.times do |element|
            result << generate_pascal_number(row_index, element)
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
