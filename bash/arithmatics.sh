# Given two integers,  and , find their sum, difference, product, and quotient.
read first
read last
echo `expr $first + $last`
echo `expr $first - $last`
# note the expression format
echo `expr $(($first * $last))`
echo `expr $first / $last`
