# PermMissingElem
##Find the missing element in a given permutation
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(a)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

```ruby
def solution(a)
  # write your code in Ruby 2.2
  size_of_a = a.size
  return 1 if size_of_a.zero?
  
  sum_of_array = a.inject(&:+)
  expected_sum = ((size_of_a + 1) *(size_of_a + 2)) / 2
  expected_sum - sum_of_array
end
```