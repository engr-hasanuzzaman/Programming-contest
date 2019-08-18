# https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def birthday(s, d, m)
  s_index = 0
  step = m
  e_index = s.size - m
  count = 0

  while s_index <= e_index
    if s[s_index...s_index+m].sum == d
      count += 1
    end

    s_index += 1 
  end

  count
end
