# CountDiv
### Compute number of integers divisible by k in range [a..b].
### Task description
Write a function:

def solution(a, b, k)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.

```ruby
def solution(a, b, k)
  return 0 if k > b
  return b - a + 1 if k == 1

  first_div_num = if a > k 
                    if a % k == 0
                      a
                    else
                      rem = a % k
                      a + (k - rem)
                    end
                  else
                    k
                  end
   #puts "--#{first_div_num}"             
   num_of_d_num = 1
   a_num = (b - first_div_num) / k
   #puts "---a_num #{a_num}, #{num_of_d_num}"
   num_of_d_num = num_of_d_num + a_num
   #puts "===== #{num_of_d_num}"

  num_of_d_num
end
```